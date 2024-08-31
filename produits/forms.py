from django import forms
from .models import Produit

class ProduitForm(forms.ModelForm):
    
    prix=forms.FloatField()
    class Meta:
        model= Produit
        fields=['nom','description','prix','image']

    def clean_prix(self):
        prix= self.cleaned_data.get('prix')

        if prix < 0 or prix==0 or prix == None or prix=='':
            raise forms.ValidationError('Le prix doit etre supérieur a 0')
        return prix