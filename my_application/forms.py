from django import forms 
from .models import Users

class UserForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['firstname', 'lastname', 'age', 'email', 'phone_number']
        widgets = {
            'firstname': forms.TextInput(attrs={'class': 'form-control'}),
            'lastname': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone_number': forms.NumberInput(attrs={'class': 'form-control'}),
        }