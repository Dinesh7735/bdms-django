from django.db import models
from django.conf import settings
# Create your models here.



class DonorProfile(models.Model):

    BLOOD_GROUP_CHOICES = (('A+', 'A+'),('A-', 'A-'),
                           ('B+', 'B+'),('B-', 'B-'),
                           ('AB+', 'AB+'),('AB-', 'AB-'),
                           ('O+', 'O+'),('O-', 'O-'),)
    
    GENDER_CHOICES = (('male', 'Male'),
                      ('female', 'Female'),
                      ('other', 'Other'),)

    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    blood_group = models.CharField(max_length=5,choices=BLOOD_GROUP_CHOICES)
    gender = models.CharField(max_length=10,choices=GENDER_CHOICES)
    age = models.PositiveIntegerField()
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to='donors/',default='default.png')
    availability_status = models.BooleanField(default=True)
    last_donation_date = models.DateField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):

        return self.user.full_name