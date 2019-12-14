from django.contrib import admin
from .models import Item, Nak, Snu, Mirim, Forever
# Register your models here.

class NakAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'date','st_period', 'fin_period' ]
    list_display_links = ['id', 'name']
admin.site.register(Nak, NakAdmin)

class SnuAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'date','st_period', 'fin_period' ]
    list_display_links = ['id', 'name']
admin.site.register(Snu, SnuAdmin)

class MirimAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'date','st_period', 'fin_period' ]
    list_display_links = ['id', 'name']
admin.site.register(Mirim, MirimAdmin)

class ForeverAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'date','st_period', 'fin_period' ]
    list_display_links = ['id', 'name']
admin.site.register(Forever, ForeverAdmin)

admin.site.register(Item)
