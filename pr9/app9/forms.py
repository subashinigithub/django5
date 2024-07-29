from django import forms
from.models import Document

class DocumentForm(forms.ModelForm):
    class Meta:
        model=Document
        fields=['title','image','pdf']

class dataform(forms.Form):
    username=forms.CharField(max_length=255)
    password=forms.CharField(max_length=255)