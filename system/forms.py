from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User

#ФОРМЫ РЕГИСТРАЦИИ И ВХОДА (ОНИ ВСТРОЕНЫ В ДЖАНГО)
class UserLoginForm(AuthenticationForm):
    username = UsernameField(label='Имя пользователя', widget=forms.TextInput())
    password = forms.CharField(label='Пароль', strip=False, widget=forms.PasswordInput())

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя')
    password1 = forms.CharField(label="Пароль", strip=False, widget=forms.PasswordInput())
    password2 = forms.CharField(label="Повторите пароль", strip=False, widget=forms.PasswordInput())
    email = forms.EmailField(label='Почта')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
