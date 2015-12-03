from django.contrib import admin
from main.models import Dvd, Genre, Studio
# Register your models here.
class DvdAdmin(admin.ModelAdmin):
    search_fields =['title']
    list_display = ('title', 'studio')

class GenreAdmin(admin.ModelAdmin):
    search_fields =['genre']

class StudioAdmin(admin.ModelAdmin):
    search_fields =['studio']
admin.site.register(Dvd, DvdAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Studio, StudioAdmin)