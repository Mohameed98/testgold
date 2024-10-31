# datasetapp/forms.py
from django import forms

class DateRangeForm(forms.Form):
    start_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}), label=" from ")
    end_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}), label=" to ")
