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
from treatment.views import service, doctor, payment, whomToServe, uploadedfiles, uploadFiles, confirmation, services, protocols, detailed_view
from user.views import authorization, registration, activate_account, profile, alert
from treatment.services import request_add, doctor_add, patient_add, research_add, pay, protocol_viewing, complete_viewing
from doctor_cabinet.views import doctor_cabinet, doctors_request, analysis_request, completed_request
from doctor_cabinet.services import request_accept, continue_analysis, complete_analysis, review_analysis # report_add
from treatment.reverse_addressing import to_services, to_researches, to_confirming, to_doctors, to_patients

urlpatterns = [
    # users interface pages
    path('admin/', admin.site.urls),
    path('service/', service, name='service'),
    path('doctor/', doctor, name='doctor'),
    path('toserve/', whomToServe, name='whomToServe'),
    path('upload/', uploadFiles, name='uploadfiles'),
    path('confirmation/', confirmation, name='confirmation'),
    path('payment/', payment, name='payment'),
    path('services/', services, name='services'),
    path('uploadedfiles/', uploadedfiles, name='uploadedfiles'),
    path('protocols/', protocols, name='protocols'),
    path('detailed_view/', detailed_view, name='detailed_view'),

    # making users
    path('authorization/', authorization, name='authorization'),
    path('registration/', registration, name='registration'),
    path('', profile, name='profile'),

    # users interface logic
    path('request_add/', request_add, name='request_add'),
    path('doctor_add/', doctor_add, name='doctor_add'),
    path('patient_add/', patient_add, name='patient_add'),
    path('research_add/', research_add, name='research_add'),
    path('pay/', pay, name='pay'),
    path('protocol_viewing/<int:request_id>', protocol_viewing, name='protocol_viewing'),
    path('complete_viewing/<int:request_id>', complete_viewing, name='complete_viewing'),

    # doctors interface logic
    path('request_accept/<int:request_id>', request_accept, name='request_accept'),
    path('continue_analysis/<int:request_id>', continue_analysis, name='continue_analysis'),
    path('complete_analysis/<int:request_id>', complete_analysis, name='complete_analysis'),
    path('review_analysis/<int:request_id>', review_analysis, name='review_analysis'),
    # path('report_add/', report_add, name='report_add'),

    # doctors interface pages
    path('doctor_cabinet/', doctor_cabinet, name='doctor_cabinet'),
    path('doctors_request/', doctors_request, name='doctors_request'),
    path('analysis_request/', analysis_request, name='analysis_request'),
    path('completed_request/', completed_request, name='completed_request'),

    # reverse addressing of users interface
    path('to_services/', to_services, name='to_services'),
    path('to_researches/', to_researches, name='to_researches'),
    path('to_confirming/', to_confirming, name='to_confirming'),
    path('to_doctors/', to_doctors, name='to_doctors'),
    path('to_patients/', to_patients, name='to_patients'),

    # email confirming
    path('activate/<str:uidb64>/<str:token>/', activate_account, name='activate'),
    path('alert/', alert, name='alert'),
]


# adding media and static urls (IF DEBUGING)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)