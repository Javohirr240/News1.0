from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Profile


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email', 'password1', 'password2')

# class UserRegisterForm(forms.ModelForm):
#     password1 = forms.CharField(label='Parol',
#                                 widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Parolni takrorlang',
#                                 widget=forms.PasswordInput)
#
#     class Meta:
#         model = User
#         fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
#
#     def clean_password(self):
#         data = self.cleaned_data
#         if data['password1'] != data['password2']:
#             raise forms.ValidationError("Parolini takrorlashda xatolik ketdi(password==password2)!")
#         return data['password1']



class UserRegisterForm(UserCreationForm):
    password1 = forms.CharField(label='Parol', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Parolni takrorlang', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 != password2:
            raise forms.ValidationError('Passwords don\'t match')
        return password2

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name','email')
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('phone_number','birth_date','avatar')



















