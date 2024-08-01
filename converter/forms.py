from django import forms

class ConverterForm(forms.Form):
    amount = forms.FloatField(required=True, initial=1)
    from_currency = forms.CharField(max_length=50)
    to_currency = forms.CharField(max_length=50)