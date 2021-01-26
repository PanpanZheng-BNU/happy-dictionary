from django import forms


class TranslationForm(forms.Form):
    q = forms.CharField(label="", widget=forms.TextInput(
        attrs={'id': 'translate_text', 'class': 'form-control', 'placeholder': "输入您不认识的单词"}), max_length=50)

class TranslationForm2(forms.Form):
    q2 = forms.CharField(label="", widget=forms.TextInput(
        attrs={'id': 'translate_text2', 'class': 'form-control', 'rows':"3",'placeholder': "输入您不认识的单词"}), max_length=50)
