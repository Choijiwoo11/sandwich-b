# from django.contrib.auth.models import User
from django import forms
from sandwich.models import Category, User


class RegisterForm(forms.ModelForm):
    email = forms.CharField(label='이메일',widget=forms.EmailInput)
    password = forms.CharField(label='비밀번호', widget=forms.PasswordInput)
    password2 = forms.CharField(label='비밀번호 확인', widget=forms.PasswordInput)


    class Meta:
        model = User
        fields = ['last_name', 'first_name', 'username','password','password2', 'email','phone', 'birthdate']

    def clean_password2(self):
        cd = self.cleaned_data

        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords not matched')
        return cd['password2']
