from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from . import models

ADMIN = 1
VIP = 2
GUEST = 3
USER = 4
USER_CHOICE = (
    (ADMIN, 'ADMIN'),
    (VIP, 'VIP'),
    (GUEST, 'GUEST'),
    (USER, 'USER')
)
MALE = 1
FEMALE = 2
GENDER_TYPE = (
    (MALE, 'MALE'),
    (FEMALE, 'FEMALE')
)


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True)
    age = forms.IntegerField(required=True)
    user_choice = forms.ChoiceField(choices=USER_CHOICE, required=True)
    country = forms.CharField(required=True)
    gender = forms.ChoiceField(choices=GENDER_TYPE, required=True)
    height = forms.IntegerField(required=True)
    weight = forms.IntegerField(required=True)
    user_job = forms.CharField(required=True)

    class Meta:
        model = models.CustomUser
        fields = (
            'username',
            'email',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'age',
            'user_type',
            'gender',
            'country',
            'height',
            'weight',
            'user_job'
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

    username = UsernameField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'username',
            'id': 'hello'}
    ))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'email',
            'id': 'hell'}
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'password',
            'id': 'hi'}
    ))
