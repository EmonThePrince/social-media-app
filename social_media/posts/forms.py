from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):  # Form for user registration
    email = forms.EmailField()  # Email field for user registration

    class Meta:  # Meta options for the UserRegisterForm
        model = User
        fields = ['username', 'email', 'password1', 'password2']  # Fields included in the registration form
