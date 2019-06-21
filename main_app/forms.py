from django.forms import ModelForm, PasswordInput, Form, CharField
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User 

class LoginForm(Form):
    username = CharField(label="User Name", max_length=64)
    password = CharField(widget=PasswordInput())