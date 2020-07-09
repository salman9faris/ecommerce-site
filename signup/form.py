from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib import messages


class CustomUserCreationForm(forms.Form):
    first_name = forms.CharField(label='enter first name', widget= forms.TextInput
                           (attrs={'placeholder':'Enter your first name', 'class': 'form-control'}) ,max_length=100)
    last_name = forms.CharField(label='enter first name',max_length=100,widget= forms.TextInput
                           (attrs={'placeholder':'Enter your last name', 'class': 'form-control'}) )
    username = forms.CharField(label='enter username', widget= forms.TextInput
                           (attrs={'placeholder':'Enter username', 'class': 'form-control'}),max_length=100, )
    email = forms.EmailField(label='entr email id',max_length=100,widget= forms.EmailInput
                           (attrs={'placeholder':'Enter email id', 'class': 'form-control'}))
    password1 = forms.CharField(label='entr password', max_length=100 , widget= forms.PasswordInput
                           (attrs={'placeholder':'password' , 'class': 'form-control'}))
    password2 = forms.CharField(label='confrm password',max_length=100, widget=forms.PasswordInput
                           (attrs={'placeholder':'confrom password' , 'class': 'form-control'}))

    def clean_password2(self):
        password1=self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise ValidationError("password doesn't match")
        return password1




    def save(self, Commit= True):
        user=User.objects.create_user(
            username=self.cleaned_data['username'],
            last_name=self.cleaned_data['last_name'],
            first_name=self.cleaned_data['first_name'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password1'],
        )
        return user

    def clean_username(self):
        username=self.cleaned_data['username']
        r=User.objects.filter(username=username)
        if r.count():
            raise ValidationError("username already exist")
        return username

