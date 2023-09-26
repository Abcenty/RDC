from django.shortcuts import HttpResponseRedirect
from treatment.models import Requests, Researches
from user.models import Services, Patients
from django.urls import reverse
from treatment.forms import PatientChoosingForm, UserResearchAddForm
from datetime import date