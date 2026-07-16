from django.shortcuts import render,redirect
from django.contrib.auth import login, logout, authenticate
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from .forms import AppointmentForm
from django.contrib import messages
from .models import Appointment, Notification
from django.contrib.admin.views.decorators import staff_member_required
from django.http import JsonResponse
from django.contrib import admin
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .forms import AdminPatientForm


 # Create your views here.
def home(request):

    if request.user.is_authenticated:

        notifications = Notification.objects.filter(
            user=request.user,
            is_read=False
        ).order_by("-created_at")


        return render(
            request,
            "patient_home.html",
            {
                "notifications": notifications
            }
        )

    else:

        return render(
            request,
            "landing.html"
        )

def register(request):

    if request.method == "POST":

        print("POST DATA:")
        print(request.POST)

        form = RegisterForm(request.POST)

        print("VALID:", form.is_valid())
        print("ERRORS:", form.errors)

        if form.is_valid():
            form.save()
            return redirect("login")

    else:
        form = RegisterForm()

    return render(request,"register.html",{"form":form})

def login_view(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password,
        )

        if user is not None:

            login(request, user)

            # If user is admin/superuser
            if user.is_superuser or user.is_staff:
                return redirect("admin_dashboard")

            # Otherwise normal patient
            else:
                return redirect("home")

        else:
            messages.error(
                request,
                "Invalid username or password."
            )

    return render(request, "login.html")

def logout_view(request):

    logout(request)

    return redirect("home")


@login_required
def appointment(request):

    if request.method == "POST":

        form = AppointmentForm(request.POST)

        if form.is_valid():

            appointment = form.save(commit=False)

            appointment.user = request.user

            appointment.save()


            admins = User.objects.filter(
                is_staff=True
            )


            for admin in admins:

                Notification.objects.create(
                    user=admin,
                    message=f"New appointment from {request.user.username} for {appointment.service}"
                )


            return redirect("appointment_success")


    else:

        form = AppointmentForm()


    return render(
        request,
        "appointment.html",
        {
            "form": form
        }
    )


@login_required
def patient_home(request):

    notifications = Notification.objects.filter(
        user=request.user,
        is_read=False
    ).order_by("-created_at")


    return render(
        request,
        "patient_home.html",
        {
            "notifications":notifications
        }
    )

@staff_member_required
def admin_dashboard(request):

    appointments = Appointment.objects.all().order_by("-created_at")


    notifications = Notification.objects.filter(
        user=request.user
    ).order_by("-created_at")


    unread = notifications.filter(
        is_read=False
    ).count()



    context={

        "appointments":appointments,

        "notifications":notifications,

        "unread":unread

    }


    return render(
        request,
        "admin_dashboard.html",
        context
    )


@staff_member_required
def update_appointment_status(request,id,status):


    appointment=get_object_or_404(
        Appointment,
        id=id
    )


    if appointment.status != status:

        appointment.status = status

        appointment.save()


        Notification.objects.create(

            user=appointment.user,

            message=f"Your {appointment.service} appointment has been {status}"

        )


    return redirect(
        "admin_dashboard"
    )


@staff_member_required
def delete_appointment(request, id):

    appointment = get_object_or_404(
        Appointment,
        id=id
    )

    appointment.delete()

    return redirect("admin_dashboard")

@login_required
def my_appointments(request):

    appointments = Appointment.objects.filter(
        user=request.user
    ).order_by("-created_at")


    return render(
        request,
        "my_appointments.html",
        {
            "appointments":appointments
        }
    )


@login_required
def appointment_success(request):

    return render(
        request,
        "appointment_success.html"
    )
@login_required
def patient_notifications(request):

    notifications = Notification.objects.filter(
        user=request.user
    ).order_by("-created_at")


    return render(
        request,
        "patient_notifications.html",
        {
            "notifications": notifications
        }
    )
@login_required
def patient_appointment_status(request):

    appointments = Appointment.objects.filter(
        user=request.user
    ).order_by("-created_at")


    data=[]


    for appointment in appointments:

        data.append({

            "id": appointment.id,

            "service": appointment.service,

            "date": str(appointment.appointment_date),

            "time": str(appointment.appointment_time),

            "status": appointment.status

        })


    return JsonResponse(
        {
            "appointments":data
        }
    )
@staff_member_required
def admin_appointments_update(request):

    appointments = Appointment.objects.all().order_by("-created_at")


    data=[]


    for appointment in appointments:


        data.append({

            "id":appointment.id,

            "username":appointment.user.username,

            "phone":appointment.phone_number,

            "service":appointment.service,

            "date":str(appointment.appointment_date),

            "time":str(appointment.appointment_time),

            "status":appointment.status

        })


    return JsonResponse(
        {
            "appointments":data
        }
    )
@staff_member_required
def delete_all_appointments(request):

    if request.method == "POST":

        Appointment.objects.all().delete()

    return redirect("admin_dashboard")





@staff_member_required
def add_patient(request):

    if request.method == "POST":

        form = AdminPatientForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data["username"]

            user, created = User.objects.get_or_create(
                username=username
            )


            appointment = form.save(commit=False)

            appointment.user = user

            appointment.status = "Approved"

            appointment.save()


            return redirect("admin_dashboard")


    else:

        form = AdminPatientForm()


    return render(
        request,
        "add_patient.html",
        {
            "form":form
        }
    )
@staff_member_required
def delete_notification(request,id):

    notification = get_object_or_404(
        Notification,
        id=id,
        user=request.user
    )

    notification.delete()

    return redirect("admin_dashboard")