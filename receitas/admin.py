from django.contrib import admin

from .models import Receita

# Classe para manupular a exibição no modo adimin das receitas criadas
class ListandoReceitas(admin.ModelAdmin):
    # Tupla de quais colunas devem aparecer no editar receitas
    list_display: list|tuple = ('id', 'nome_receita', 'categoria', 'tempo_preparo' )
    # Tupla de quais colunas possuirão links
    list_display_links: list|tuple = ('id','nome_receita')
    # Campo de busca
    search_fields: list|tuple = ('nome_receita',)
    # Limite por página
    list_per_page: int = 2
    # Filtro
    list_filter: list|tuple = ('categoria',)

admin.site.register(Receita, ListandoReceitas)
