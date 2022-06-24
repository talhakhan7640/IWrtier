from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms.utils import ErrorList


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=120, required=True, label='', widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control', 'autocomplete': 'off'}))
    email = forms.EmailField(required=True, label='', widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'form-control', 'autocomplete': 'off'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control', 'autocomplete': 'off'}), label='')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password', 'class': 'form-control','autocomplete': 'off'}), label='', help_text='')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# class UserLoginForm(forms.ModelForm):
#     username = forms.CharField(max_length=120, required=True, label='', widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control', 'autocomplete': 'off'}))
#     password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control', 'autocomplete': 'off'}), label='')


class DivErrorList(ErrorList):
    def __str__(self):
        return self.as_divs()

    def as_divs(self):
        if not self:
            return ''
        return '<div class="errorlist">%s</div>' % ''.join(['<div class="error alert alert-danger mt-1">%s</div>' % e for e in self])




# ------------Main form--------------


# class UserRegistrationForm(UserCreationForm):
#     email = forms.EmailField(required=True, label="", widget=forms.TextInput({ "placeholder": "Email"}))
    
#     def __init__(self, *args, **kwargs):
#         super(UserRegistrationForm, self).__init__(*args, **kwargs)

#         for fieldname in ['username', 'password1', 'password2']:
#             self.fields[fieldname].help_text = None
#             self.fields[fieldname].label = ""

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']