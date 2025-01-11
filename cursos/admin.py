from django.contrib import admin
from cursos.models import Curso

class listandoCursos(admin.ModelAdmin):
    list_display = ("id", "nome", "legenda", "publicado", "data_publicacao")
    list_display_links = ("id", "nome")
    search_fields = ("nome",)
    list_filter = ("categoria", "usuario",)
    list_editable = ("publicado",)
    list_per_page = 10

admin.site.register(Curso, listandoCursos)