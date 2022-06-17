from django import forms

from app1.models import task


class updateform(forms.ModelForm):
    class Meta:
        model=task
        fields=['name','priority','date']

