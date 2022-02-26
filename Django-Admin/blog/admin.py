from django.contrib import admin
from mdeditor.fields import MDTextField
from mdeditor.widgets import MDEditorWidget

from .models import *

# Register your models here.

# class PostInline(admin.TabularInline):
#    model = Post


class PostStackedInline(admin.StackedInline):
    model = Post


class PostAdmin(admin.ModelAdmin):

    formfield_overrides = {models.TextField: {"widget": MDEditorWidget}}

    list_display = ("titulo", "descricao", "data_cadastro", "data_edicao", "autor")

    list_filters = ("data_cadastro", "data_edicao")

    search_fields = ("titulo", "autor")


class AutorAdmin(admin.ModelAdmin):
    list_display = ("nome", "email")

    search_fields = ("nome", "email")

    # inlines = (PostInline,)

    inlines = (PostStackedInline,)


admin.site.register(Post, PostAdmin)
admin.site.register(Autor, AutorAdmin)
