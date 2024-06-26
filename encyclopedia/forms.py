from django import forms

class MyForm(forms.Form):
    q = forms.CharField()

class NewPageForm(forms.Form):
    title = forms.CharField(max_length=150)
    content = forms.CharField(widget=forms.Textarea)
    
class EditPageForm(forms.Form):
    title = forms.CharField(widget=forms.HiddenInput(), max_length=150)
    content = forms.CharField(widget=forms.Textarea)