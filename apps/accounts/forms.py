from django import forms
from .models import User
import re

class RegisterForm(forms.ModelForm):

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control'
            }
        )
    )

    confirm_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control'
            }
        )
    )

    class Meta:

        model = User

        fields = [
            'full_name',
            'email',
            'phone_number',
        ]

        widgets = {

            'full_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter full name'
                }
            ),

            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter email address'
                }
            ),

            'phone_number': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter phone number'
                }
            ),
        }

    def clean(self):

        cleaned_data = super().clean()

        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:

            raise forms.ValidationError(
                "Passwords do not match"
            )

        return cleaned_data
    
    def clean_full_name(self):

        full_name = self.cleaned_data.get('full_name')

        if not re.match(r'^[A-Za-z ]+$', full_name):

            raise forms.ValidationError(
                "Name should contain only alphabets and spaces"
            )

        return full_name


    def clean_phone_number(self):

        phone_number = self.cleaned_data.get('phone_number')

        if not phone_number.isdigit():

            raise forms.ValidationError(
                "Phone number should contain digits only"
            )

        if len(phone_number) != 10:

            raise forms.ValidationError(
                "Phone number must be exactly 10 digits"
            )

        return phone_number


    def clean_email(self):

        email = self.cleaned_data.get('email')

        allowed_domains = [
            '.com',
            '.in',
            '.org',
            '.net'
        ]

        if not any(email.endswith(domain) for domain in allowed_domains):

            raise forms.ValidationError(
                "Enter a valid email domain"
            )

        return email

class LoginForm(forms.Form):

    email = forms.EmailField(

        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter email'
            }
        )
    )

    password = forms.CharField(

        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter password'
            }
        )
    )