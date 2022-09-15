from django.shortcuts import get_object_or_404, get_list_or_404, render
from .models import Receita

def index(request):  # Verificar como que é utilizado, no método indica o uso de um parâmetro o rquest, mas seu uso não adiciona o parâmetro aparente menete, no arquivo url.py
    
    receita = Receita.objects.order_by('-date_receita').filter(publicada=True)
    
    dados = {
        'receitas' : receita
    }

    return render(request, 'receitas/index.html', dados)

def receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)

    receita_a_exibir = {
        'receita':receita
    }

    return render(request, 'receitas/receita.html', receita_a_exibir)

def buscar(request):
    lista_receita = Receita.objects.order_by('-date_receita').filter(publicada=True)

    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']

        if buscar:
            lista_receita = lista_receita.filter(nome_receita__icontains=nome_a_buscar)

    dados = {
        'receitas': lista_receita
    }
    return render(request, 'receitas/buscar.html', dados)