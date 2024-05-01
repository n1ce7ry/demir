from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import CustomUser


class LoginForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password']
        
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(
            attrs={'class': 'login__input', 'placeholder': 'Логин'}
        )
        self.fields['username'].label = False
        self.fields['password'].widget = forms.PasswordInput(
            attrs={'class': 'login__input', 'placeholder':'Пароль'}
        ) 
        self.fields['password'].label = False


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['login',
                  'first_name', 
                  'last_name',
                  'phone',
                  'password',
                  'passport_details',
                  'email']
        widgets = {
            'login': forms.TextInput(attrs={'class': 'registration__input', 'placeholder': 'Логин'}),
            'first_name': forms.TextInput(attrs={'class': 'registration__input', 'placeholder': 'Имя'}),
            'last_name': forms.TextInput(attrs={'class': 'registration__input', 'placeholder': 'Фамилия'}),
            'phone': forms.TextInput(attrs={'class': 'registration__input', 'placeholder': 'Телефон'}),
            'password': forms.TextInput(attrs={'class': 'registration__input', 'type': 'password', 'placeholder': 'Пароль'}),
            'passport_details': forms.TextInput(attrs={'class': 'registration__input', 'placeholder': 'Серия и номер паспорта'}),
            'email': forms.TextInput(attrs={'class': 'registration__input', 'type': 'email', 'placeholder': 'Почта'}),
        }