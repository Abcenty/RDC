from django.shortcuts import render

# Create your views here.
def service(request):
    # ваш код обработчика
    return render(request, 'treatment/Applications/Service.html')

def doctor(request):
    # ваш код обработчика
    return render(request, 'treatment/Applications/Doctor.html')
