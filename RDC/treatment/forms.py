from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms
from .models import Users, Patients
from treatment.models import Requests, Researches
from doctor_cabinet.models import Report


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


class UserResearchAddForm(UserChangeForm):
    research_file = forms.FileField(widget=forms.FileInput, required=False)

    class Meta:
        model = Researches
        fields = ('research_file',)


class UserConfirmationForm(forms.ModelForm):
    service = forms.CharField(widget=forms.TextInput(attrs={'readonly': True , "class": "px-3 py-1 border border-blue-300 rounded-lg focus:outline-blue-200 w-5/12 bg-white" }))
    patient = forms.CharField(widget=forms.TextInput(attrs={'readonly': True, "class": "px-3 py-1 border border-blue-300 rounded-lg focus:outline-blue-200 w-5/12 bg-white" }))
    doctor = forms.CharField(widget=forms.TextInput(attrs={'readonly': True, "class": "px-3 py-1 border border-blue-300 rounded-lg focus:outline-blue-200 w-5/12 bg-white" }))
    research = forms.CharField(widget=forms.TextInput(attrs={'readonly': True, "class": "px-3 py-1 border border-blue-300 rounded-lg focus:outline-blue-200 w-5/12 bg-white" }))


    class Meta:
        model = Requests
        fields = ('service', 'patient', 'doctor', 'research') # 'files'