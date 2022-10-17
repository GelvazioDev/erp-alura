from django.contrib import admin
from setup_producao.models import Setup

@admin.register(Setup)
class SetupAdmin(admin.ModelAdmin):
    list_display = ('id','instrutor',)
    list_display_links = ('id', 'instrutor',)
    search_fields = ('instrutor',)
    list_per_page = 25
