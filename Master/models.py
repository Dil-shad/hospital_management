
from django.db import models
from django.contrib import admin
# Create your models here.


from django.contrib.auth.models import User
from tomlkit import date

# departments = [('Cardiologist', 'Cardiologist'),
#                ('Dermatologists', 'Dermatologists'),
#                ('Emergency Medicine Specialists',
#                 'Emergency Medicine Specialists'),
#                ('Allergists/Immunologists', 'Allergists/Immunologists'),
#                ('Anesthesiologists', 'Anesthesiologists'),
#                ('Colon and Rectal Surgeons', 'Colon and Rectal Surgeons')
#                ]


class Docter_dep(models.Model):
    department = models.CharField(
        max_length=50, null=True, blank=True)

    def __str__(self):
        return self.department


class DoctorModel(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20, null=True)
    is_status = models.BooleanField(default=False)
    qualification = models.CharField(max_length=100, null=True, blank=True)
    department = models.ForeignKey(
        Docter_dep, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(
        upload_to='profile_pic/DoctorProfilePic/', null=True, blank=True)

    def __str__(self):
        return self.user.first_name


class PatientModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10)
    age = models.CharField(max_length=3)
    gender = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    bloodgroup = models.CharField(max_length=10)
    case = models.CharField(max_length=10)
    # otp=models.CharField(max_length=6)
    # verify=models.CharField(max_length=1,default=0)
    image = models.ImageField(
        upload_to='profile_pic/PatientProfilePic/', null=True, blank=True)

    def __str__(self):
        return self.user.first_name


class AppoinmentModel(models.Model):
    doc = models.CharField(max_length=10)
    visiter = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.CharField(max_length=15)

    def __str__(self):
        return self.visiter


class PayModel(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    fees = models.CharField(max_length=20, null=True, blank=True)
    salary = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.fees
