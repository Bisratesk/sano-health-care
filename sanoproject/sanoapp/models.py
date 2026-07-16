
# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin


class Appointment(models.Model):

    SERVICE_CHOICES = [
        ("General Checkup", "General Checkup"),
        ("senior homecare", "Senior Homecare"),
        ("medicalconsultation", "Medical Consultation"),
        ("tubechanges", "Tube Changes"),
        ("woundcare", "Wound Care"),
        ("chronicdisease", "Chronic Disease"),
    ]


    STATUS_CHOICES = (
        ("Pending", "Pending"),
        ("seen", "Seen"),
        ("Approved", "Approved"),
        ("Rejected", "Rejected"),
        ("Completed", "Completed"),
    )


    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    phone_number = models.CharField(
        max_length=20
    )


    service = models.CharField(
        max_length=100,
        choices=SERVICE_CHOICES
    )


    appointment_date = models.DateField()


    appointment_time = models.TimeField()


    message = models.TextField(
        blank=True
    )


    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Pending"
    )


    seen = models.BooleanField(
        default=False
    )


    created_at = models.DateTimeField(
        auto_now_add=True
    )
  


    def __str__(self):

        return f"{self.user.username} - {self.service}"
    
   
class Notification(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    message = models.TextField()

    is_read = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):

        return f"{self.user.username} - {self.message}"
from django.db import models


