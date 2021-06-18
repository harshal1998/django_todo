from django import forms
from .models import *


class todoform(forms.ModelForm):
    add = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Add item'}))

    class Meta:
        model = todo
        fields = "__all__"
