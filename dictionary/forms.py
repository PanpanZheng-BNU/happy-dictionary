from django import forms

# translate input form
class TranslationForm(forms.Form):
    q = forms.CharField(label="", widget=forms.TextInput(
        attrs={'id': 'input-text', 'class': 'form-control', 'placeholder': "输入您不认识的单词"}), max_length=50)
