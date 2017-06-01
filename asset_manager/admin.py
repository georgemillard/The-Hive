from django.contrib import admin
from . import models
from . forms import FileForm

class FileAdmin(admin.ModelAdmin):
    form = FileForm

# Register your models here.
admin.site.register(models.Folder)
admin.site.register(models.File, FileAdmin)
