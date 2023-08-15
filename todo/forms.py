from django.forms import ModelForm
from django import forms
from .models import Todo


class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ('text',)
        labels = {
            'text':'',
        }
        widgets = {
            'text':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter todo e.g. Delete junk files'}),
        }