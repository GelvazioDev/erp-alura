from django.contrib import admin
from artigos.models import Artigo

@admin.register(Artigo)
class ArtigoAdmin(admin.ModelAdmin):
    list_display = ('id_do_artigo','titulo', 'link_doc', 'status')
    list_display_links = ('id_do_artigo', 'titulo',)
    search_fields = ('id_do_artigo', 'titulo',)
    list_filter = ('categoria', 'status', )
    ordering = ('-id_do_artigo',)
    list_editable = ('status',)
    list_per_page = 25
