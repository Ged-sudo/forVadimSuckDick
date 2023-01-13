from django.contrib import admin
from . import models

class MenueAdmin(admin.ModelAdmin):
    list_display = ['pk', 'menue_choices', 'count', 'date_sale']
    list_editable = ['menue_choices', 'count']

admin.site.register(models.MenueDonar, MenueAdmin)

