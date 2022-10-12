from django.contrib import admin
from django.urls import path

admin.site.site_header  =  "Alura ERP Front-end"  
admin.site.index_title  =  "Pessoas, contatos, artigos, alura+, cursos e formações da escola de Front-end"
admin.site.site_title =  "ERP - Front-end"

urlpatterns = [
    path('', admin.site.urls),
]
