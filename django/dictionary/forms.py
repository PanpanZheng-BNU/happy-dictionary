from django import forms


class TranslationForm(forms.Form):
    q = forms.CharField(label="", widget=forms.TextInput(
        attrs={'id': 'translate_text', 'class': 'form-control', 'placeholder': "输入您不认识的单词"}), max_length=50)
