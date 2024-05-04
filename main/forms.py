from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import CustomUser
from rental.models import Proposal


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
                  'fio',
                  'phone',
                  'password',
                  'passport_details',
                  'email',]
        widgets = {
            'login': forms.TextInput(attrs={'class': 'registration__input', 'placeholder': 'Логин'}),
            'fio': forms.TextInput(attrs={'class': 'registration__input', 'pattern':'[А-Яа-я]*?\s[А-Яа-я]*?\s[А-Яа-я]*', 'placeholder': 'ФИО'}),
            'phone': forms.TextInput(attrs={'class': 'registration__input', 'minlength':'11', 'pattern': '\+7[0-9]+', 'placeholder': 'Телефон в формате +7'}),
            'password': forms.PasswordInput(attrs={'class': 'registration__input', 'minlength': '6', 'placeholder': 'Пароль'}),
            'passport_details': forms.TextInput(attrs={'class': 'registration__input', 'minlength': '10', 'placeholder': 'Серия и номер паспорта'}),
            'email': forms.EmailInput(attrs={'class': 'registration__input', 'pattern': '([A-z0-9_.-]{1,})@([A-z0-9_.-]{1,}).([A-z]{2,8})', 'placeholder': 'Почта'}),
        }


class ProposalForm(forms.ModelForm):
    class Meta:
        model = Proposal
        fields = ['date_start', 'date_end']
        widgets = {
            'date_start': forms.DateInput(
                attrs={
                    'onchange': "calculatePrice('{{ car.id }}', '{{ car.price }}')",
                    'class': 'modal__date',
                    'id': 'start_{{ car.id }}',
                    'value':'{{ today }}',
                    'name': 'trip-start',
                    'min': '{{ today }}',
                }
            ),
            'date_start': forms.DateInput(
                attrs={
                    'onchange': "calculatePrice('{{ car.id }}', '{{ car.price }}')",
                    'class': 'modal__date',
                    'id': 'end_{{ car.id }}',
                    'value':'{{ tomorrow }}',
                    'name': 'trip-end',
                    'min': '{{ tomorrow }}',
                }
            ),
        }