from django import forms
from .models import Abiturient, Univer


class AbiturientForm(forms.ModelForm):
    class Meta:
        model = Abiturient
        fields = '__all__'


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UniverForm(forms.ModelForm):
    class Meta:
        model = Univer
        fields = "__all__"