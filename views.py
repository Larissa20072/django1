from django.shortcuts import render, redirect
from .models import Tarefa
from .forms import TarefaForm
from django.urls import reverse

def index_view(request):
    all_tarefas = Tarefa.objects.all()
    context = {
        'title': 'página principal',
        'tarefas': all_tarefas
    }
    return render(request, 'tarefas/index.html', context )


def form_view(request):
    form_action = reverse('adicionar')
    
    if request.method == 'POST':
        form = TarefaForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TarefaForm() 

    context = {
        'title': 'Adicionar Tarefa',
        'form': form,
        'form_action': form_action
    }
    return render(request, 'tarefas/form.html', context )

def delete_view(request, id_tarefa):
    tarefa= Tarefa.objects.get(id=id_tarefa)
    
    if tarefa:
        tarefa.delete()
    
    return redirect('index')
