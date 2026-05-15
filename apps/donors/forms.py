from django import forms
from .models import DonorProfile


class DonorProfileForm(forms.ModelForm):
    class Meta:
        model = DonorProfile
        exclude = ['user','created_at','updated_at',]
        widgets = {'blood_group': forms.Select(attrs={'class': 'form-select'}),
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'age': forms.NumberInput(attrs={'class': 'form-control','placeholder': 'Enter age'}),
            'address': forms.Textarea(attrs={'class': 'form-control','placeholder': 'Enter address','rows': 3}),
            'city': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter city'}),
            'state': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter state'}),
            'profile_image': forms.FileInput(attrs={'class': 'form-control'}),
            'availability_status': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'last_donation_date': forms.DateInput(attrs={'class': 'form-control','type': 'date'}),
        }