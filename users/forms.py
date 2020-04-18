from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Profile


CATEGORY_CHOICE = [('Customer', 'Customer'), ('Company', 'Company')]


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1',
                  'password2']


class ProfileForm(forms.ModelForm):
    user_category = forms.CharField(label='Please select Atleast One', widget=forms.Select(choices=CATEGORY_CHOICE),
                                    required=True)

    class Meta:
        model = Profile
        fields = ['user_category' , 'image']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

