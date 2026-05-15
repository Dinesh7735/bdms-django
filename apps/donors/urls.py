from django.urls import path
from .views import create_donor_profile

urlpatterns = [
    path('create-profile/',create_donor_profile,name='create_donor_profile'),
]