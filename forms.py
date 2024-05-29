from django import forms
from .models import Tarefa

class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = ['titulo', 'descricao']
        
        widgets = {
            'titulo': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Adicione um titulo'}
            ),
            'descricao': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': 'Adicione um descrição'}
            ),
        }
