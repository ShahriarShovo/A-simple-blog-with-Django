from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from App_login.models import UserProfile

class SignUpForm(UserCreationForm):
    email=forms.EmailField(required=True)
    class Meta:
        model=User
        fields=('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

class UserChangeProfile(UserChangeForm):
    class Meta:
        model=User
        fields=('username','email', 'first_name', 'last_name', 'password')

class ChangeProfilePicture(forms.ModelForm):
    class Meta:
        model=UserProfile
        fields= ['profile_pic',]