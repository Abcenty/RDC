from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms
from .models import Users
from treatment.models import Requests, Researches
from doctor_cabinet.models import Report


class DoctorReportAddForm(UserChangeForm):
    file = forms.FileField(widget=forms.FileInput, required=False)
    comment = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Введите результат исследования',
         'class': 'border-blue-500 w-full mb-2 p-2 border rounded-md break-words h-32'
        }))

    class Meta:
        model = Report
        fields = ('file', 'comment',)