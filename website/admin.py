from django.contrib import admin
from .models import *

class LeadAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'registered_on')
    search_fields = ( 'email', 'registered_on' )

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'address','note', 'received_at')
    search_fields = ( 'name', 'email', 'address', 'note' )

admin.site.register(Lead, LeadAdmin)
admin.site.register(Cause)
admin.site.register(EventCategory)
admin.site.register(Event)
admin.site.register(Contact, ContactAdmin)