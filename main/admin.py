from django.contrib import admin
from main.models import Dvd
# Register your models here.
class DvdAdmin(admin.ModelAdmin):
    search_fields =['title']
    list_display = ('title', 'studio')
admin.site.register(Dvd, DvdAdmin)