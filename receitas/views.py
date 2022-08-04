from django.shortcuts import render

def index(request):  # Verificar como que é utilizado, no método indica o uso de um parâmetro o rquest, mas seu uso não adiciona o parâmetro aparente menete, no arquivo url.py
    return render(request, 'index.html')
