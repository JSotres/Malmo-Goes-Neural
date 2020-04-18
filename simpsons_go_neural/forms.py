from django import forms
from .models import SimpsonCharacter


class SimpsonForm(forms.ModelForm):
    class Meta:
        model = SimpsonCharacter
        fields = ('simpson_input_picture',)
