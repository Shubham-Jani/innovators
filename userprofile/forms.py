from userprofile.models import Profile
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
import sys
sys.path.append('../')


class UserForm(UserCreationForm):

    input_class = 'text-gray-800 border-2 border-gray-700 rounded-lg focus:outline-none block w-full p-2.5'

    password1 = forms.CharField(
        label="Password", widget=forms.PasswordInput(attrs={'class': input_class}))
    password2 = forms.CharField(
        label="Password", widget=forms.PasswordInput(attrs={'class': input_class}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        input_class = 'text-gray-800 border-2 border-gray-700 rounded-lg focus:outline-none block w-full p-2.5'

        widgets = {
            # 'password1': forms.TextInput(attrs={'type': 'password', 'class': input_class}),
            # 'password2': forms.TextInput(attrs={'type': 'password', 'class': input_class}),
            'username': forms.TextInput(attrs={'class': input_class}),
            'email': forms.TextInput(attrs={'class': input_class}),
        }

        def save(self, commit=False):
            user = super().save(commit=False)

            user.email = self.cleaned_data['email']
            if commit:
                user.save()
            return user


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('age', 'gender', 'marital_status',
                  'income_class', 'cast_class', 'education_class')
        input_class = 'text-gray-800 border-2 border-gray-700 rounded-lg focus:outline-none block w-full p-2.5'
        widgets = {
            'gender': forms.Select(attrs={'class': input_class}),
            'income_class': forms.Select(attrs={'class': input_class}),
            'age': forms.DateInput(attrs={'class': input_class, 'type': 'number'}),
            'marital_status': forms.Select(attrs={'class': input_class}),
            'cast_class': forms.Select(attrs={'class': input_class}),
            'education_class': forms.Select(attrs={'class': input_class}),
        }



class UpdateUserForm(forms.ModelForm):
    input_class = 'text-gray-800 border-2 border-gray-700 rounded-lg focus:outline-none block w-full p-2.5'
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': input_class}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': input_class}))

    class Meta:
        model = User
        fields = ['username', 'email']

