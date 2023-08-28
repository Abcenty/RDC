from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
    

from .models import Users, Patients
from treatment.models import Requests


class PatientChoosingForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите имя'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите фамилию'}))
    patronymic = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите отчество'}))
    SNILS = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите СНИЛС'}))
    Passport = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите серию и номер паспорта'}))
    # birthCertificateNumber = forms.CharField(widget=forms.NumberInput(attrs={'placeholder': 'Введите номер свидетельства о рождении'}))
    birthDate =  forms.CharField(widget=forms.DateTimeInput(attrs={'placeholder': 'Введите дату рождения'}))

    class Meta:
        model = Patients
        fields = ('last_name', 'first_name', 'patronymic', 'birthDate', 'SNILS', 'Passport')


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
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите имя пользователя'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите имя'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите фамилию'}))
    patronymic = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите отчество'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите номер телефона'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Введите адрес электронной почты'}))
    SNILS = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите СНИЛС'}))
    Passport = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите серию и номер паспорта'}))
    # birthCertificateNumber = forms.CharField(widget=forms.NumberInput(attrs={'placeholder': 'Введите номер свидетельства о рождении'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Введите подтверждение пароля'}))
    birthDate =  forms.CharField(widget=forms.DateTimeInput(attrs={'placeholder': 'Введите дату рождения'}))

    class Meta:
        model = Users
        fields = ('password1', 'password2', 'username', 'last_name', 'first_name', 'phone', 'patronymic', 'birthDate', 'email', 'SNILS', 'Passport')

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