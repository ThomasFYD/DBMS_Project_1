# school_data/forms.py
from django import forms
from .models import SchoolData

class SchoolDataForm(forms.ModelForm):
    class Meta:
        model = SchoolData
        fields = '__all__'  # Or specify fields you want to include

