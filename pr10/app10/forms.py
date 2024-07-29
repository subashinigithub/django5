from django import forms
from .models import students
from django.contrib.auth.forms import AuthenticationForm

class stuform(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=students
        fields=['name','age','Qualifcation','Grade','Group','EmailId','password']



class studentloginform(AuthenticationForm):
    username=forms.EmailField(label='Email')