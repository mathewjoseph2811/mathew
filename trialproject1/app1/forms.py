from django import forms
from .models import table1

class movieform(forms.ModelForm):
    class Meta:
        model=table1
        fields=['name','desc','details','img']