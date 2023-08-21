from django.shortcuts import render

# Create your views here.
def service(request):
    return render(request, 'treatment/Applications/Service.html')

def doctor(request):
    return render(request, 'treatment/Applications/Doctor.html')

def whomToServe(request):
    return render(request, 'treatment/Applications/WhomToServe.html')

def uploadFiles(request):
    return render(request, 'treatment/Applications/UploadFiles.html')

def confirmation(request):
    return render(request, 'treatment/Applications/Confirmation.html')

def payment(request):
    return render(request, 'treatment/Applications/Payment.html')

def services(request):
    return render(request, 'treatment/Services/services.html')

def uploadedfiles(request):
    return render(request, 'treatment/UploadedFiles/uploadedfiles.html')
