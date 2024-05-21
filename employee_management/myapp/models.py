from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# Create your models here.
class Employee(models.Model):
    emp_no = models.IntegerField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=555)
    emp_start_date = models.DateField(default="MM/DD/YYYY")
    emp_end_date = models.DateField(null=True, blank=True)
    photo = models.ImageField(upload_to='employee_photos/', null=True, blank=True)
    status = models.CharField(max_length=20)

    def __str__(self):
        return self.name
   

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.user.username