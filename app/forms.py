from django import forms

# import JeetuModel from models.py
from .models import JeetuModel

# create a ModelForm


class JeetuForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = JeetuModel
        fields = "__all__"
