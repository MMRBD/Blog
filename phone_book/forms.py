from django import forms
from .models import PhoneBook


class PhoneBookForms(forms.ModelForm):
    class Meta:
        model = PhoneBook
        fields = ["name", "email", "mobile", "phone", "city", "address", "country"]
