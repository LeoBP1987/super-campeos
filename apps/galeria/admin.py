from django.contrib import admin
from apps.galeria.models import Categorias, Campeonatos, Times

class ListarCategorias(admin.ModelAdmin):
    list_display = ('id', 'nome', 'pontos', 'publicado')
    list_display_links = ('id', 'nome')
    list_editable = ('pontos', 'publicado')
    list_filter = ('nome',)
    list_per_page = 10

class ListarCampeonatos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'categoria', 'nivel', 'publicado')
    list_display_links = ('id', 'nome')
    list_editable = ('nivel', 'publicado')
    list_filter = ('nome', 'categoria')
    list_per_page = 10

class ListarTimes(admin.ModelAdmin):
    list_display = ('id', 'nome', 'local', 'publicado')
    list_display_links = ('id', 'nome', 'publicado')
    list_filter = ('nome', 'local')
    list_per_page = 10

admin.site.register(Categorias, ListarCategorias)
admin.site.register(Campeonatos, ListarCampeonatos)
admin.site.register(Times, ListarTimes)
