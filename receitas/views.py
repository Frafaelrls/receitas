from django.shortcuts import get_object_or_404, get_list_or_404, render
from .models import Receita

def index(request):  # Verificar como que é utilizado, no método indica o uso de um parâmetro o rquest, mas seu uso não adiciona o parâmetro aparente menete, no arquivo url.py
    
    receita = Receita.objects.all()
    
    dados = {
        'receitas' : receita
    }

    return render(request, 'index.html', dados)

def receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)

    receita_a_exibir = {
        'receita':receita
    }

    return render(request, 'receita.html', receita_a_exibir)