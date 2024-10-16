from django import forms 

class KeyWordForm(forms.Form):
    keyword = forms.CharField(max_length=2000)
    number = forms.IntegerField(min_value=1)
    