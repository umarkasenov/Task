from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models

GENDER_CHOICES = (
        ("M", "Мужской"),
        ("F", "Женский"),
        ("IT", "Другое")
    )
STATUS_CHOICES = (
        ("В сети", "В сети"),
        ("Занят", "Занят"),
        ("На работе", "На работе"),
        ("В школе", "В школе")
    )


class CustomRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    age = forms.IntegerField(required=True)
    gender = forms.ChoiceField(required=True, choices=GENDER_CHOICES)
    status = forms.ChoiceField(required=True, choices=STATUS_CHOICES)
    phone_number = forms.CharField(required=True)
    avatar = forms.ImageField(required=True)
    bio = forms.CharField(required=True)
    social_media = forms.URLField(required=True)
    interests = forms.CharField(required=True)
    hobbies = forms.CharField(required=True)

    class Meta:
        model = models.CustomUser
        fields = [
            'username',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'age',
            'gender',
            'status',
            'phone_number',
            'avatar',
            'bio',
            'social_media',
            'interests',
            'hobbies',
        ]

    def save(self, commit=True):
        user = super(CustomRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.status = self.cleaned_data['status']
        if commit:
            user.save()
        return user
