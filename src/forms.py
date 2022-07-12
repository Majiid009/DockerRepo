from django.contrib.auth.forms import UserCreationForm
from django import forms
from accounts.models import CustomUser

class CustomSignupForm(UserCreationForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'Your Email', "class" : "CreationInput"}),)
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder':'Enter your password', "class" : "CreationInput"}),
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder':'Repeat your password', "class" : "CreationInput"}),
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder':'Your Username', "class" : "CreationInput"}),
    )
    
    class Meta :
        model = CustomUser
        fields = ("email", "username", )