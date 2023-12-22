from django import forms
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User

class UserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'last_name', 'first_name', 'password1', 'password2')


class ProfileForm(forms.ModelForm):

    birthday = forms.DateField(widget=forms.DateInput)

    class Meta:
        model = Profile
        fields = ('birthday', 'tel')