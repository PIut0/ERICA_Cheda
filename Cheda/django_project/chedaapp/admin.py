from django.contrib import admin
from .models import Item, Nak, Snu
# Register your models here.

class NakAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'date','st_period', 'fin_period' ]
    list_display_links = ['id', 'name']
admin.site.register(Nak, NakAdmin)

class SnuAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'date','st_period', 'fin_period' ]
    list_display_links = ['id', 'name']
admin.site.register(Snu, SnuAdmin)



admin.site.register(Item)
