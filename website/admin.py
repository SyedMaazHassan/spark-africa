from django.contrib import admin
from . import models


class LeadAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'registered_on')
    search_fields = ( 'email', 'registered_on' )


admin.site.register(models.Lead, LeadAdmin)