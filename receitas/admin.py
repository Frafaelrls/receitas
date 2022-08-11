from django.contrib import admin

from .models import Receita

# Classe para definir a nomenclatura para as receitas criadas
class ListandoReceitas(admin.ModelAdmin):
    # Tupla de quais colunas devem aparecer no editar receitas
    list_display = ('id', 'nome_receita', 'categoria', 'tempo_preparo' )
    # Tupla de quais colunas possuirão links
    list_display_links = ('id','nome_receita')

admin.site.register(Receita, ListandoReceitas)
