from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Appointment

class RegisterForm(forms.ModelForm):

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter username"
            }
        )
    )


    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "id": "password",
                "placeholder": "Enter password"
            }
        )
    )


    class Meta:

        model = User

        fields = [
            "username",
            "password"
        ]


    def save(self, commit=True):

        user = super().save(commit=False)

        user.set_password(
            self.cleaned_data["password"]
        )

        if commit:
            user.save()

        return user

class AppointmentForm(forms.ModelForm):

    class Meta:

        model = Appointment

        fields = [
            'phone_number',
            'service',
            'appointment_date',
            'appointment_time',
           
        ]

        widgets = {

            "phone_number": forms.TextInput(
                attrs={
                    "type": "tel",
                    "placeholder": "+251 9XX XXX XXX",
                    "required": True
                }
            ),


            "appointment_date": forms.DateInput(
                attrs={
                    "type": "date"
                }
            ),


            "appointment_time": forms.TimeInput(
                attrs={
                    "type": "time"
                }
            )

        }


class AdminPatientForm(forms.ModelForm):

    username = forms.CharField(
        max_length=100
    )


    appointment_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                "type": "date"
            }
        )
    )


    appointment_time = forms.TimeField(
        widget=forms.TimeInput(
            attrs={
                "type": "time"
            }
        )
    )



    class Meta:

        model = Appointment

        fields = [
            "username",
            "phone_number",
            "service",
            "appointment_date",
            "appointment_time",
        ]