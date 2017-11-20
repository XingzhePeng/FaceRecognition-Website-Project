from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import auth
from django.contrib.auth import logout
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from itsdangerous import URLSafeTimedSerializer as utsr
import base64
from django.conf import settings as django_settings
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from django.http import JsonResponse


class Token:
    def __init__(self, security_key):
        self.security_key = security_key
        byte_security_key = security_key.encode(encoding="utf-8")
        self.salt = base64.encodebytes(byte_security_key)

    def generate_validate_token(self, username):
        serializer = utsr(self.security_key)
        return serializer.dumps(username, self.salt)

    def confirm_validate_token(self, token, expiration=900):
        serializer = utsr(self.security_key)
        return serializer.loads(token, salt=self.salt, max_age=expiration)

    def over_validate_token(self, token):
        serializer = utsr(self.security_key)
        print(serializer.loads(token, salt=self.salt))
        return serializer.loads(token, salt=self.salt)

token_confirm = Token(django_settings.SECRET_KEY)


def welcome(request):
    return render(request, 'welcome/welcome.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        if not User.objects.filter(username=username):
            if not User.objects.filter(email=username):
                json_si = {'code_si': 1}#不存在
                return JsonResponse(json_si)
            else:
                user=User.objects.get(email=username)
        else:
            user = User.objects.get(username=username)
        if not check_password(password, user.password):
            json_si = {'code_si': 2}
            return JsonResponse(json_si)#密码错误
        if not user.is_active:
            email = user.email
            json_si = {'code_si': 3, 'email': email}
            return JsonResponse(json_si)#未激活
        logout(request)
        auth.login(request, user)
        json_si = {'code_si': 4}
        return JsonResponse(json_si)#成功
    else:
        return render(request, 'welcome/welcome.html')


#接收注册参数并发送邮件
def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        if User.objects.filter(username=username):
            return HttpResponse(1)#用户名已注册
        if User.objects.filter(email=email):
            return HttpResponse(2)#邮箱已注册
        user = User.objects.create_user(username=username, email=email, password=password)
        user.is_active = False
        user.save()
        token = token_confirm.generate_validate_token(username)
        subject = u'Account Activation-Face Master'
        message = "\n\n".join(
            [u'Dear {0}, you are receiving this email because you signed up for Face Master earlier'.format(username),
             u'To activate your account, please click on the link below',
             '/'.join(['http://123.206.213.40/activate', token])])
        while True:
            num = send_mail(subject, message, django_settings.EMAIL_HOST_USER, [email], fail_silently=False)
            if num == 1:
                break
        return HttpResponse(3)#成功
    else:
        return render(request, 'welcome/welcome.html')


#点击注册邮件
def activate(request, token):
    try:
        username = token_confirm.confirm_validate_token(token)
        user = User.objects.get(username=username)
        if user.is_active:
            json_a = {'code_a': 1}
            return render(request, 'welcome/welcome.html', {'json_a': json_a})  # 已经激活过了
        user.is_active = True
        user.save()
        json_a = {'code_a': 2}
        return render(request, 'welcome/welcome.html', {'json_a': json_a}) #激活成功
    except:
        username = token_confirm.over_validate_token(token)
        user = User.objects.get(username=username)
        if user.is_active:
            json_a = {'code_a': 1}
            return render(request, 'welcome/welcome.html', {'json_a': json_a})  # 已经激活过了
        email = user.email
        json_a = {'code_a': 3, "email": email}
        return render(request, 'welcome/welcome.html', {'json_a': json_a})#激活超时


#重发激活邮件
def sendemail_a(request):
    if request.method == 'POST':
        email = request.POST.get('email', None)
        username = User.objects.get(email=email).username
        token = token_confirm.generate_validate_token(username)
        subject = u'Account Activation-Face Master'
        message = "\n\n".join([u'Dear {0}, you are receiving this email because you signed up for Face Master earlier'.format(username),
                               u'To activate your account, please click on the link below',
                               '/'.join(['http://123.206.213.40/activate', token])])
        while True:
            num = send_mail(subject, message, django_settings.EMAIL_HOST_USER, [email], fail_silently=False)
            if num == 1:
                break
        return HttpResponse(1)#发送激活邮件成功
    else:
        return render(request, 'welcome/welcome.html')


#发送重置密码邮件
def reset(request):
    if request.method == 'POST':
        email = request.POST.get('email', None)
        try:
             user = User.objects.get(email=email)
        except User.DoesNotExist:
            return HttpResponse(1)#用户不存在
        username = user.username
        token = token_confirm.generate_validate_token(username)
        subject = u'Password Reset-Face Master'
        message = "\n\n".join([u'Dear {0}, you are receiving this email because you clicked "Forgot password" on our website'.format(username),
                               u'To reset your password, please click on the link below',
                               '/'.join(['http://123.206.213.40/reset_au', token])])
        while True:
            num = send_mail(subject, message, django_settings.EMAIL_HOST_USER, [email], fail_silently=False)
            if num == 1:
                break
        return HttpResponse(2)  # 发送重置邮件成功
    else:
        return render(request, 'welcome/welcome.html')


#点击重置邮件里的链接
def reset_au(request, token):
    try:
        username = token_confirm.confirm_validate_token(token)
        json_r = {'code_r': 1, 'username': username}
        return render(request, 'welcome/welcome.html', {'json_r': json_r})  # 验证成功
    except:
        username = token_confirm.over_validate_token(token)
        email = User.objects.get(username=username).email
        json_r = {'code_r': 2, "email": email}
        return render(request, 'welcome/welcome.html', {'json_r': json_r})  # 验证超时


def reset_done(request):
    username = request.POST.get('username', None)
    new_password = request.POST.get('password', None)
    user = User.objects.get(username=username)
    user.password = make_password(new_password)
    user.save()
    return HttpResponse(1)#改密成功


def page_not_found(request):
    return render(request, 'welcome/not_found.html')


def server_error(request):
    return render(request, 'welcome/server_error.html')