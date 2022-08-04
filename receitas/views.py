from django.shortcuts import render
from .models import Receita

def index(request):  # Verificar como que é utilizado, no método indica o uso de um parâmetro o rquest, mas seu uso não adiciona o parâmetro aparente menete, no arquivo url.py
    
    receita = Receita.objects.all()
    
    dados = {
        'receitas' : receita
    }

    return render(request, 'index.html', dados)

def receita(request):
    return render(request, 'receita.html')