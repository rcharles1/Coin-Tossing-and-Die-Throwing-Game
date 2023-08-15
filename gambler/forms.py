from django import forms

class SingleInputForm(forms.Form):
    input_field = forms.CharField()
