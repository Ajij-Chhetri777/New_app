from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from quiz.models import Account
from django.contrib.auth.models import User
class RegisterForm(UserCreationForm):
    # username = forms.CharField(
    #     label='Username',
    #     max_length=150,
    #     help_text=''  # Set help_text to an empty string
    # )

    # # Customize password field
    # password1 = forms.CharField(
    #     label='Password',
    #     widget=forms.PasswordInput,
    #     help_text=''  # Set help_text to an empty string
    # )
    # password2 = forms.CharField(
    #     label='Confirm Your Password',
    #     widget=forms.PasswordInput,
    #     help_text=''  # Set help_text to an empty string
    # )
    class Meta:
       model = User
       fields = ['username','password1','password2']
class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        model = ['username','password']

class AccForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = '__all__'