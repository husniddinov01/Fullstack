from django import forms
from .models import User, Group


class UserForm(forms.ModelForm):
    class Meta():
        model = User
        fields = '__all__'


class LoginForm(forms.ModelForm):
    class Meta():
        model = User
        fields = ('username', 'password')


class GroupForm(forms.ModelForm):
    class Meta():
        model = Group
        fields = '__all__'