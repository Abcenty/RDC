from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from .models import Users, Services
from treatment.models import Requests
from django import forms


class ServiceChoiceForm(forms.ModelForm):
    service = forms.ModelChoiceField(queryset=Services.objects.all(), label='Услуги')

    class Meta:
        model = Requests
        fields = ('service',)



class UserLoginForm(AuthenticationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Введите адрес электронной почты'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль'}))

    class Meta:
        model = Users
        fields = ('email', 'password')

    """def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        for field_name, filed in self.fields.items():
            filed.widget.attrs['class'] = 'form-control py-4'"""


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите имя'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите фамилию'}))
    patronymic = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите отчество'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Введите адрес электронной почты'}))
    SNILS = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Введите СНИЛС'}))
    Passport = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Введите серию и номер паспорта'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Подтвердите пароль'}))

    class Meta:
        model = Users
        fields = ('first_name', 'last_name', 'patronymic', 'email', 'SNILS', 'Passport', 'password1', 'password2')

"""    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        for field_name, filed in self.fields.items():
            filed.widget.attrs['class'] = 'form-control py-4'"""


"""class UserProfileForm(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'readonly': True}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'readonly': True}))

    class Meta:
        model = Users
        fields = ('username', 'email', 'first_name', 'last_name')

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        for field_name, filed in self.fields.items():
            filed.widget.attrs['class'] = 'form-control py-4'"""
