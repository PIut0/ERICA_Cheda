from django.contrib import admin
from .models import Item, Nak
# Register your models here.

class NakAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'date','st_period', 'fin_period' ]
    list_display_links = ['id', 'name']
admin.site.register(Nak, NakAdmin)
admin.site.register(Item)
