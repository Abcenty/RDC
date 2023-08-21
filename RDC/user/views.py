from django.shortcuts import render
# Create your views here.

def authorization(request):
    return render(request, 'user/Authorization/authorization.html')

def registration(request):
    return render(request, 'user/Registration/registration.html')