from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth, messages
from django.urls import reverse
from user.forms import UserLoginForm, UserRegistrationForm
# Create your views here.

"""def authorization(request):
    return render(request, 'user/Authorization/authorization.html')

def registration(request):
    return render(request, 'user/Registration/registration.html')"""



def authorization(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = auth.authenticate(email=email, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('service'))
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'user/Authorization/authorization.html', context)

def registration(request):
    if request.method == "POST":
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрировались!')
            return HttpResponseRedirect(reverse('user/Authorization/authorization.html'))
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'user/Registration/registration.html', context)
