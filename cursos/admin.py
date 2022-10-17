from django.contrib import admin
from cursos.models import Curso
from django.utils.html import format_html

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('id_do_curso','nome', 'categoria', 'instrutor', 'projeto', 'pasta_do_curso_url', 'status',)
    list_display_links = ('id_do_curso', 'nome', 'pasta_do_curso_url',)
    search_fields = ('id_do_curso', 'nome',)
    list_filter = ('categoria', 'status','trimestre', 'ano', )
    ordering = ('-id_do_curso',)
    list_editable = ('status',)
    list_per_page = 25

    def pasta_do_curso_url(self, obj):
        return format_html("<a href='{url}' target='_blank'>{url}</a>", url=obj.pasta_do_curso)


