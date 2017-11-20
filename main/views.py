from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .tasks import *
from django.contrib.auth.models import User
import os
from django.http import HttpResponseRedirect
from django.conf import settings as django_settings
from django.http import HttpResponse
from django.contrib.auth import logout


PIC_PATH = os.path.join(django_settings.BASE_DIR, 'PIC')


@login_required
def main(request):
    user_name = request.user.username
    pics = Picture.objects.order_by('-date')
    pics = pics.filter(username=user_name)
    iterator_date = None
    send_pics = []
    for pic in pics:
        if pic.date != iterator_date:
            iterator_date = pic.date
            date_every = {}
            date_every['date'] = iterator_date
            pics_date = []
            pics_date.append(pic.picname)
            date_every['pics_date'] = pics_date
            send_pics.append(date_every)
        else:
            pics_date.append(pic.picname)
    return render(request, 'main/main.html', {'send_pics': send_pics})


@login_required
def account(request):
    user_name = request.user.username
    user = User.objects.get(username=user_name)
    return render(request, 'main/account.html', {'user': user})


@login_required
def about(request):
    return render(request, 'main/about.html')


@login_required
def pic(request, picname):
    user_name = request.user.username
    pic_faces = PicFace.objects.filter(username=user_name, source_pic=picname, is_identified=1)
    # faces = []
    # for pic_face in pic_faces:
    #     face_spe = Face.objects.get(username=user_name, uid=pic_face.uid)
    #     if face_spe in faces:
    #         continue
    #     else:
    #         faces.append(face_spe)
    pic = Picture.objects.get(picname=picname)
    return render(request, 'main/bigpic.html', {'pic_faces': pic_faces, 'pic': pic})


@login_required
def delete(request, picname):
    user_name = request.user.username
    pic_faces = PicFace.objects.filter(username=user_name, source_pic=picname)
    for pic_face in pic_faces:
        uid = pic_face.uid
        small = pic_face.small_pic
        test_uid_pics = PicFace.objects.filter(username=user_name, uid=uid)
        test_sourse = []
        for test_uid_pic in test_uid_pics:
            sourse = test_uid_pic.source_pic
            if sourse not in test_sourse:
                test_sourse.append(sourse)
        if len(test_uid_pics)>1 and len(test_sourse)>1:#should not delete Face object
            if os.path.exists(os.path.join(PIC_PATH, small)):
                os.remove(os.path.join(PIC_PATH, small))
            pic_face.delete()
            face = Face.objects.get(username=user_name, uid=uid)
            if face.show_pic == small:#check if the show_pic was in the photo to be deleted
                face.show_pic = PicFace.objects.filter(username=user_name, uid=uid).first().small_pic
                face.save()
        else:
            if os.path.exists(os.path.join(PIC_PATH, small)):
                os.remove(os.path.join(PIC_PATH, small))
            pic_face.delete()
            Face.objects.get(username=user_name, uid=uid).delete()
            aipFace.deleteGroupUser(user_name, uid)
            time.sleep(0.5)
    if os.path.exists(os.path.join(PIC_PATH, picname)):
        os.remove(os.path.join(PIC_PATH, picname))
    Picture.objects.get(username=user_name, picname=picname).delete()
    return HttpResponseRedirect('/main')



@login_required
def upload(request):
    user_name = request.user.username
    if request.method == 'POST':
        imgs = request.FILES.getlist('newpics')
        for img in imgs:
            (shotname, extension) = os.path.splitext(img.name)
            pic_name = shotname+'_'+user_name+extension
            try:
                Picture.objects.get(picname=pic_name)
                continue
            except:
                new_img = Picture(
                    username=user_name,
                    picname=pic_name,
                )
                with open(os.path.join(PIC_PATH, pic_name), "wb+") as destination:
                    for chunk in img.chunks():
                        destination.write(chunk)
                new_img.save()
        recog.delay(user_name)
        return HttpResponseRedirect('/main')


@login_required
def faces(request):
    user_name = request.user.username
    faces = Face.objects.filter(username=user_name)
    return render(request, 'main/faces.html', {'faces': faces})


@login_required
def if_add_face(request):
    if request.method == 'POST':
        user_name = request.user.username
        face_before = int(request.POST.get("num_of_faces", "0"))
        face_now = len(Face.objects.filter(username=user_name))
        if face_now > face_before:
            return HttpResponse(1)#人脸数增加
        return HttpResponse(2)


@login_required
def oneface(request, small_pic):
    user_name = request.user.username
    uid = PicFace.objects.get(username=user_name, small_pic=small_pic).uid
    face_pics = PicFace.objects.filter(username=user_name, uid=uid, is_identified=1)
    return render(request, 'main/face_pic.html', {'face_pics': face_pics, 'small_pic': small_pic})


@login_required
def re_identify(request):
    user_name = request.user.username
    re_identify_task.delay(user_name)
    return HttpResponseRedirect('/main/faces/')


@login_required
def signout(request):
    logout(request)
    return HttpResponseRedirect('/')
