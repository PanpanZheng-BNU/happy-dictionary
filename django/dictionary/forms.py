from django import forms

class TaskForm(forms.Form):
    task_domain = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control','placeholder':"請在這裏輸入文字",'style':"font-family:'UDDi-B'"}), max_length=50)
