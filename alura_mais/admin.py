from django.contrib import admin
from alura_mais.models import Alura_mais

@admin.register(Alura_mais)
class AluraMaisAdmin(admin.ModelAdmin):
    list_display = ('id','titulo', 'categoria', 'instrutor','status')
    list_display_links = ('id', 'titulo',)
    search_fields = ('id', 'titulo',)
    list_filter = ('categoria', 'status', )
    ordering = ('-id',)
    list_editable = ('status',)
    list_per_page = 25
