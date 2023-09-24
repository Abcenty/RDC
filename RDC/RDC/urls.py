"""
URL configuration for RDC project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path
from treatment.views import service, doctor, payment, whomToServe, uploadedfiles, uploadFiles, confirmation, services
from user.views import authorization, registration, activate_account, profile, alert
from treatment.services import request_add, doctor_add, patient_add, research_add, pay
from doctor_cabinet.views import doctor_cabinet, doctors_request, analysis_request, completed_request
from doctor_cabinet.services import request_accept, continue_analysis, complete_analysis, review_analysis # report_add

urlpatterns = [
    path('admin/', admin.site.urls),
    path('service/', service, name='service'),
    path('doctor/', doctor, name='doctor'),
    path('toserve/', whomToServe, name='whomToServe'),
    path('upload/', uploadFiles, name='uploadfiles'),
    path('confirmation/', confirmation, name='confirmation'),
    path('payment/', payment, name='payment'),
    path('services/', services, name='services'),
    path('uploadedfiles/', uploadedfiles, name='uploadedfiles'),

    path('authorization/', authorization, name='authorization'),
    path('registration/', registration, name='registration'),
    path('', profile, name='profile'),

    path('request_add/', request_add, name='request_add'),
    path('doctor_add/', doctor_add, name='doctor_add'),
    path('patient_add/', patient_add, name='patient_add'),
    path('research_add/', research_add, name='research_add'),
    path('pay/', pay, name='pay'),

    path('request_accept/<int:request_id>', request_accept, name='request_accept'),
    path('continue_analysis/<int:request_id>', continue_analysis, name='continue_analysis'),
    path('complete_analysis/<int:request_id>', complete_analysis, name='complete_analysis'),
    path('review_analysis/<int:request_id>', review_analysis, name='review_analysis'),
    # path('report_add/', report_add, name='report_add'),

    path('doctor_cabinet/', doctor_cabinet, name='doctor_cabinet'),
    path('doctors_request/', doctors_request, name='doctors_request'),
    path('analysis_request/', analysis_request, name='analysis_request'),
    path('completed_request/', completed_request, name='completed_request'),

    path('activate/<str:uidb64>/<str:token>/', activate_account, name='activate'),
    path('alert/', alert, name='alert'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)