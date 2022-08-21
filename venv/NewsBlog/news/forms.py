from django import forms
from .models import News
import re
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class ViewUser(forms.ModelForm):
    model = User
    fields = ['username', 'email', 'first_name', 'last_name', 'last_login', 'date_joined']


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        exclude = ["author"]
        fields = ['title', 'preview', 'content', 'link', 'is_published', 'author']
        widgets = {
            'title':forms.TextInput(attrs={"class" : "form-control"})       ,
            'content':forms.Textarea(attrs={"class" : "form-control",}),
            'preview':forms.Textarea(attrs={"class" : "form-control", "rows" : 2}),
            'link':forms.TextInput(attrs={"class" : "form-control"}),
        }
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'class':'form=control'}))
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class':'form=control'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class':'form=control'}))
    password2 = forms.CharField(label='Подтверждение пароля', help_text=False, widget=forms.PasswordInput(attrs={'class':'form=control'}))

    class Meta():
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form=control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form=control'}))