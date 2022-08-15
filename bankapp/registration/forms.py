from django import forms

from registration.models import register, Branch


class DatePickerInput(forms.DateInput):
    input_type = 'date'

class PersonForm(forms.ModelForm):
    class Meta:
        model = register
        fields = ('name', 'dob', 'age', 'gender','phone','email','address','district','branch','account','debit','credit','cheque')
        widgets = {
            'dob': DatePickerInput(),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['branch'].queryset = Branch.objects.none()

        if 'country' in self.data:
            try:
                country_id = int(self.data.get('country'))
                self.fields['branch'].queryset = Branch.objects.filter(district_id=country_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['branch'].queryset = self.instance.country.branch_set.order_by('name')