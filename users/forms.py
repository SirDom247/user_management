from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser 

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ( 'profile_picture',
                    'date_of_birth',
                    'phone_number',
                    'state_of_origin',
                    'sex',
                    'hobbies',
                    'about_me',
                    'address',
                    'occupation',
                    'department_unit',)  # Include other fields as needed


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = (
            'username',
            'password1',
            'password2',
            'date_of_birth',
            'phone_number',
            'state_of_origin',
            'sex',
            'hobbies',
            'about_me',
            'address',
            'occupation',
            'department_unit',
            'profile_picture',
        )
