from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

# Register your models here.

@admin.register(News)
@admin.register(Teacher)
@admin.register(Science)
@admin.register(Arts)
@admin.register(Sone)
@admin.register(Junior)
@admin.register(Classe)

class ViewAdmin(ImportExportModelAdmin):
    pass