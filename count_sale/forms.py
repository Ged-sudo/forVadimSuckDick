from django import forms
from .models import MenueDonar

class AddInfoForm(forms.ModelForm):
    class Meta:
        model = MenueDonar
        fields = ["count", "menue_choices"]