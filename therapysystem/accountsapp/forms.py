from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Get Custom User model
User = get_user_model()


# 🔹 Register Form (Custom User)
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)


# 🔹 Login Form (Custom User)
class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)