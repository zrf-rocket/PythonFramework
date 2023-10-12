from django import forms
from django.contrib.auth.models import User
import re


def email_check(email):
    """
    校验邮件
    """
    pattern = re.compile(r"\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)\"?")
    return re.match(pattern, email)


class RegistrationForm(forms.Form):
    username = forms.CharField(label="UserName", max_length=60)
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Password Confirmation", widget=forms.PasswordInput)

    def clean_username(self):
        pass

    def clean_email(self):
        pass

    def clean_password1(self):
        pass

    def clean_password2(self):
        pass


class LoginForm(forms.Form):
    username = forms.CharField(label='UserName', max_length=60)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    def clean_username(self):
        pass


class ProfileForm(forms.Form):
    pass


class PwdChangeForm(forms.Form):
    pass