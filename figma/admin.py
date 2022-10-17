from django.contrib import admin
from figma.models import Figma
from django.utils.html import format_html

@admin.register(Figma)
class FigmaAdmin(admin.ModelAdmin):
    list_display = ('id','nome', 'descricao', 'link_figma_url', 'mobile', 'status',)
    list_display_links = ('id', 'nome', 'link_figma_url',)
    search_fields = ('nome',)
    list_filter = ('status', 'mobile',)
    list_editable = ('status',)
    list_per_page = 25

    def link_figma_url(self, obj):
        return format_html("<a href='{url}' target='_blank'>{url}</a>", url=obj.link_figma)
