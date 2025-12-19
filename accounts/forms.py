from django import forms
from django.contrib.auth.models import User
from captcha.fields import CaptchaField

class RegisterForm(forms.ModelForm):
    captcha = CaptchaField()

    phone = forms.CharField()
    city = forms.CharField()
    age = forms.IntegerField()
    school = forms.CharField()
    hobby = forms.CharField()
    telegram = forms.CharField()
    address = forms.CharField()
    passport_number = forms.CharField()

    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean(self):
        cleaned = super().clean()
        if cleaned['password'] != cleaned['password2']:
            raise forms.ValidationError("Пароли не совпадают")
