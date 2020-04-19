from django import forms
from .models import SimpsonCharacter


class SimpsonForm(forms.Form):
    simpson_input_picture = forms.ImageField()
