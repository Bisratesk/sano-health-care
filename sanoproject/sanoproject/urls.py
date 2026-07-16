"""
URL configuration for sanoproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django import views
from django.contrib import admin
from django.urls import path
from sanoapp.views import home
from sanoapp.views import register, login_view, logout_view,appointment,patient_home,admin_dashboard,update_appointment_status,delete_appointment,my_appointments
from sanoapp.views import appointment_success,patient_notifications
from sanoapp.views import patient_appointment_status,admin_appointments_update
from sanoapp.views import delete_all_appointments
from sanoapp.views import add_patient
from sanoapp.views import delete_notification

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path("register/", register, name="register"),
    path("login/",login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path('appointment/',appointment,name='appointment'),
    path('patient_home/', patient_home, name='patient_home'),
    path("admin-dashboard/",admin_dashboard,name="admin_dashboard"),
    path("update-appointment/<int:id>/<str:status>/",update_appointment_status,name="update_status"),
    path("delete-appointment/<int:id>/",delete_appointment,name="delete_appointment"),
    path("my-appointments/",my_appointments,name="my_appointments"),
    path("appointment-success/",appointment_success,name="appointment_success"),
    path("notifications/",patient_notifications,name="patient_notifications"),
    path("patient-status/",patient_appointment_status,name="patient_status"),
    path("admin-updates/",admin_appointments_update,name="admin_updates"),
    path("delete-all-appointments/",delete_all_appointments,name="delete_all_appointments"),
    path("add-patient/",add_patient,name="add_patient"),
    path("delete-notification/<int:id>/",delete_notification,name="delete_notification"),

]






  
