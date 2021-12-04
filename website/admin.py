from django.contrib import admin
from .models import *

class LeadAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'registered_on')
    search_fields = ( 'email', 'registered_on' )

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'address','note', 'received_at')
    search_fields = ( 'name', 'email', 'address', 'note' )

class VolunteerRequest(admin.ModelAdmin):
    list_display = ("name", "email", "occupation", "creation_time", "is_approved")
    list_editable  = ("is_approved",)
    # search_fields = ( 'name', 'email', 'address', 'note' )



admin.site.register(Lead, LeadAdmin)
admin.site.register(Cause)
admin.site.register(EventCategory)
admin.site.register(Event)
admin.site.register(EventRegistration)
admin.site.register(Volunteer, VolunteerRequest)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Subscribe)
