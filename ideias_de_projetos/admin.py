from django.contrib import admin
from ideias_de_projetos.models import Ideia

@admin.register(Ideia)
class IdeiaAdmin(admin.ModelAdmin):
    list_display = ('ideia_em_poucas_palavras','detalhes', 'likes')
    list_display_links = ('ideia_em_poucas_palavras', 'detalhes',)
    search_fields = ('ideia_em_poucas_palavras', 'detalhes',)
    list_editable = ('likes',)
    ordering = ('-id',)
