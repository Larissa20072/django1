
from django.urls import path
from tarefas import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('adicionar',views.form_view, name='adicionar'),
    path('excluir/<int:id_tarefa>/', views.delete_view, name='excluir')
]

