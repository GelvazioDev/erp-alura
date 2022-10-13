from django.contrib import admin
from artigos.models import Artigo
from django.utils.html import format_html

@admin.register(Artigo)
class ArtigoAdmin(admin.ModelAdmin):
    list_display = ('id_do_artigo','titulo', 'link_doc_url', 'status')
    list_display_links = ('id_do_artigo', 'titulo', 'link_doc_url')
    search_fields = ('id_do_artigo', 'titulo',)
    list_filter = ('categoria', 'status', )
    ordering = ('-id_do_artigo',)
    list_editable = ('status',)
    list_per_page = 25

    def link_doc_url(self, obj):
        return format_html("<a href='{url}' target='_blank'>{url}</a>", url=obj.link_doc)
        
