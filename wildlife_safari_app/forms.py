from django import forms
from .models import Tourist

class TouristForm(forms.ModelForm):
    class Meta:
        model = Tourist
        fields = [
            'first_name',
            'second_name',
            'email',
            'nationality',
            'date',
            'phone',
            'amount'
        ]
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

