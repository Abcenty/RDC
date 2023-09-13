from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms

    

from .models import Users, Patients
from treatment.models import Requests, Researches


class PatientChoosingForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите имя',
                                                               "type": 'text',
                                                               "class": "px-3 py-1 border border-blue-300 rounded-lg focus:outline-blue-200 w-full bg-white",
                                                               "id": "firstNameInput"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите фамилию',
                                                               "type": 'text',
                                                              "class": "px-3 py-1 border border-blue-300 rounded-lg focus:outline-blue-200 w-full bg-white",
                                                               "id": "lastNameInput"}))
    patronymic = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите отчество',
                                                               "type": 'text',
                                                              "class": "px-3 py-1 border border-blue-300 rounded-lg focus:outline-blue-200 w-full bg-white",
                                                               "id": "middleNameInput"}))
    SNILS = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите СНИЛС',
                                                              "class": "px-3 py-1 border border-blue-300 rounded-lg focus:outline-blue-200 w-4/12 bg-white",
                                                               "id": "snils"}))
    Passport = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите серию и номер паспорта',
                                                              "class": "px-3 py-1 border border-blue-300 rounded-lg focus:outline-blue-200 w-6/12 bg-white",
                                                               "id": "passport"}))
    # birthCertificateNumber = forms.CharField(widget=forms.NumberInput(attrs={'placeholder': 'Введите номер свидетельства о рождении'}))
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'placeholder': 'Введите дату рождения',
                                                                "type": "date",
                                                              "class": "px-4 py-1 border border-blue-300 rounded-lg focus:outline-blue-200 w-full bg-white",
                                                               "id": "datetime"}))

    class Meta:
        model = Patients
        fields = ('last_name', 'first_name', 'patronymic') # , 'birth_date', 'SNILS', 'Passport'


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Введите имя пользователя',
        'class': 'w-full px-4 py-2 border border-slate-300 border-sky-300 rounded-lg'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Введите адрес электронной почты',
        'class': 'w-full px-4 py-2 border border-slate-300 border-sky-300 rounded-lg'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Введите пароль',
        'class': 'w-full px-4 py-2 border border-slate-300 border-sky-300 rounded-lg'}))

    class Meta:
        model = Users
        fields = ('email', 'password')

    """def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        for field_name, filed in self.fields.items():
            filed.widget.attrs['class'] = 'form-control py-4'"""


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Введите имя пользователя',
        'class': 'w-full px-4 py-2 border border-slate-300 border-sky-300 rounded-lg'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Введите имя',
        'class': 'w-full px-4 py-2 border border-slate-300 border-sky-300 rounded-lg'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Введите фамилию',
        'class': 'w-full px-4 py-2 border border-slate-300 border-sky-300 rounded-lg'}))
    patronymic = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Введите отчество',
        'class': 'w-full px-4 py-2 border border-slate-300 border-sky-300 rounded-lg'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Введите номер телефона',
        'class': 'w-full px-4 py-2 border border-slate-300 border-sky-300 rounded-lg'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Введите адрес электронной почты',
        'class': 'w-full px-4 py-2 border border-slate-300 border-sky-300 rounded-lg'}))
    SNILS = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Введите СНИЛС',
        'class': 'w-full px-4 py-2 border border-slate-300 border-sky-300 rounded-lg'}))
    Passport = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Введите серию и номер паспорта',
        'class': 'w-full px-4 py-2 border border-slate-300 border-sky-300 rounded-lg'}))
    # birthCertificateNumber = forms.CharField(widget=forms.NumberInput(attrs={'placeholder': 'Введите номер свидетельства о рождении'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Введите пароль',
        'class': 'w-full px-4 py-2 border border-slate-300 border-sky-300 rounded-lg'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Введите подтверждение пароля',
        'class': 'w-full px-4 py-2 border border-slate-300 border-sky-300 rounded-lg'}))
    birthDate = forms.DateField(widget=forms.DateInput(attrs={
        'placeholder': 'Введите дату и время рождения',
        'class': 'w-full px-4 py-2 border border-slate-300 border-sky-300 rounded-lg',
        'type': 'date'  # указываем тип ввода для HTML5
    }))

    class Meta:
        model = Users
        fields = ('password1', 'password2', 'username', 'last_name', 'first_name', 'phone', 'patronymic', 'birthDate', 'email', 'SNILS', 'Passport')


class UserProfileForm(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'readonly': True,
        'class': 'px-3 py-1 border border-blue-300 rounded-lg focus:outline-blue-200  w-8/12 mt-2 bg-white ml-auto'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'readonly': True,
        'class': 'px-3 py-1 border border-blue-300 rounded-lg focus:outline-blue-200  w-8/12 mt-2 bg-white ml-auto'
        }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'readonly': True,
        'class': 'px-3 py-1 border border-blue-300 rounded-lg focus:outline-blue-200  w-8/12 mt-2 bg-white ml-auto'
        }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'readonly': True,
        'class': 'px-3 py-1 border border-blue-300 rounded-lg focus:outline-blue-200  w-8/12 mt-2 bg-white ml-auto'}))

    class Meta:
        model = Users
        fields = ('username', 'email', 'first_name', 'last_name')


class UserConfirmationForm(forms.ModelForm):
    service = forms.CharField(widget=forms.TextInput(attrs={'readonly': True}))
    patient = forms.CharField(widget=forms.TextInput(attrs={'readonly': True}))
    doctor = forms.CharField(widget=forms.TextInput(attrs={'readonly': True}))
    research = forms.CharField(widget=forms.TextInput(attrs={'readonly': True}))


    class Meta:
        model = Requests
        fields = ('service', 'patient', 'doctor', 'research') # 'files'


class UserResearchAddForm(UserChangeForm):
    research_file = forms.FileField(widget=forms.FileInput, required=False)

    class Meta:
        model = Researches
        fields = ('research_file',)

