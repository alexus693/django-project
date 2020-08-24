from django import forms
from django.core import validators

def must_be_empty(value):
    if value:
        raise forms.ValidationError("is not empty!")

class SuggestionForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(
        attrs = {
            'class':'form-control',
        }
    ))
    email = forms.EmailField(widget=forms.TextInput(
        attrs = {
            'class':'form-control',
        }
    ))
    verify_email = forms.EmailField( label = "please verify your email address",widget=forms.TextInput(
        attrs = {
            'class':'form-control' 
        
        }
    ))
    suggestion = forms.CharField(widget=forms.Textarea(
        attrs = {
            'class':'form-control'
        }
    ))
    honeypot = forms.CharField(required=False,
                               widget=forms.HiddenInput,
                               label="Leave Empty",
                               validators=[must_be_empty])

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        verify = cleaned_data.get('verify_email')
        if email!=verify:
            raise forms.ValidationError(
                "please enter the same email in both fields"
            )                           
    

   
        
   
    