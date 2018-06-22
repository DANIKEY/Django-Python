from django import forms

class FormAuthentification(forms.Form):
    
    utilisateur  = forms.CharField(label='Utilisateur',max_length=100)
    mot_passe = forms.CharField(widget=forms.PasswordInput)
    