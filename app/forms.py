from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'image',
            'full_name', 'cpf_cnpj', 'phone', 'birth_date', 'gender',
            'cep', 'city', 'neighborhood', 'street', 'number'
        ]
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'})
        }
