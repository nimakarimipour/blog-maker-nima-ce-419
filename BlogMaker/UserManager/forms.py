from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class SignIn(forms.Form):
    username = forms.CharField(label='', max_length=100,
                               widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    error_message = ''

    def clean_username(self):
        username = self.cleaned_data['username']
        if not User.objects.filter(username=username).exists():
            self.error_message = 'user not found'
            raise ValidationError('user not found')
        return username


class SignUp(forms.Form):
    username = forms.CharField(label='', max_length=100,
                               widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    first_name = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    email = forms.CharField(label='', widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    error_message = ''

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            self.error_message = 'user already exists'
            raise ValidationError('user already exists')
        return username

    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password) < 5:
            self.error_message = 'too short password'
            raise ValidationError('too short password')
        return password


class TestForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)
    title = forms.CharField(max_length=100)

    error_message = ''

    def clean_username(self):
        username = self.cleaned_data['username']
        if username == 'nima':
            self.error_message = 'User already Exists'
            raise ValidationError('User already Exists')
        return username
