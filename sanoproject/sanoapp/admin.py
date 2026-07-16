from django.contrib import admin
from .models import Appointment, Notification

# Register your models here.
@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "service",
        "appointment_date",
        "appointment_time",
        "status",
        "seen"
    )


    list_filter = (
        "status",
        "appointment_date"
    )


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "message",
        "is_read",
        "created_at"
    )