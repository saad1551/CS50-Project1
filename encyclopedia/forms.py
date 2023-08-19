from django import forms

class MyForm(forms.Form):
    q = forms.CharField()