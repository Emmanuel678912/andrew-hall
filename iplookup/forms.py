from django.forms import ModelForm, widgets
from .models import *

from django import forms

class TableCForm(forms.ModelForm):
    class Meta:
        model = TableC
        fields = '__all__'

        widgets = {
            'column2' : forms.TextInput(attrs={'class' : 'form-control', 'style' : 'background-color : yellow;'}),
            'column3' : forms.TextInput(attrs={'class' : 'form-control', 'style' : 'background-color : yellow;'}),
            'column4' : forms.Select(attrs={'class' : 'form-control', 'style' : 'background-color : yellow;'})
        }