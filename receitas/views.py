import re
from django.shortcuts import render

def index(request):  # Verificar como que é utilizado, no método indica o uso de um parâmetro o rquest, mas seu uso não adiciona o parâmetro aparente menete, no arquivo url.py
    
    receita = {
        1:'Lasanha',
        2:'Sopa de legumes',
        3:'Sorvete',
        4: 'Bolo de chocolate'
    }
    
    dados = {
        'nome_das_receitas' : receita
    }

    return render(request, 'index.html', dados)

def receita(request):
    return render(request, 'receita.html')