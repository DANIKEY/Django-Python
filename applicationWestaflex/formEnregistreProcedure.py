from django import forms

class EnregistreForm(forms.Form):

    client = forms.CharField(label='Client',max_length=100)
    pression = forms.IntegerField()
    duree =  forms.IntegerField()
    marge = forms.IntegerField()
    diametre = forms.IntegerField()
    reference = forms.CharField(label='Reference',max_length=100)
    