from django import forms

class UserForm(forms.Form):
    email = forms.EmailInput()
    password = forms.PasswordInput()