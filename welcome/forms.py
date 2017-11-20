from django import forms


class SignUpForm(forms.Form):
    username = forms.CharField(label='username', required=True)
    email = forms.EmailField(label='email', required=True)
    password = forms.CharField(label='password', widget=forms.PasswordInput, required=True, min_length=6)
    confirm_password = forms.CharField(label='confirm_password', widget=forms.PasswordInput, required=True,
                                       min_length=6)


class SignInForm(forms.Form):
    username = forms.CharField(label='username or email', required=True)
    password = forms.CharField(label='password', widget=forms.PasswordInput, required=True)


class ResetEmail(forms.Form):
    email = forms.EmailField(label='email', required=True)


class ResetPassword(forms.Form):
    new_password = forms.CharField(label='new_password', widget=forms.PasswordInput, required=True, min_length=6)
    confirm_password = forms.CharField(label='confirm_password', widget=forms.PasswordInput, required=True,
                                       min_length=6)