from django import forms
from .models import FaceMood


class FaceForm(forms.ModelForm):

    class Meta:
        model = FaceMood
        fields = ('face_input_picture',)
