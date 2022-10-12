from django.contrib import admin
from cursos.models import Curso

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('id_do_curso','nome', 'categoria', 'instrutor', 'projeto', 'status')
    list_display_links = ('id_do_curso', 'nome',)
    search_fields = ('id_do_curso', 'nome',)
    list_filter = ('categoria', 'status', )
    ordering = ('-id_do_curso',)
    list_editable = ('status',)
    list_per_page = 25



