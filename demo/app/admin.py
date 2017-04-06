from django.contrib import admin
from .models import Contact, Wizard

class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email',)

class WizardAdmin(admin.ModelAdmin):

    list_display = ('first_name', 'last_name', 'email', 'avatar_image', 'child', 'minor', 'adult', 'adresse', 'country')
    list_filter = ('first_name', 'last_name', 'email', 'avatar_image', 'child', 'minor', 'adult', 'adresse', 'country')
    search_fields = ('first_name', 'last_name', 'email', 'avatar_image', 'child', 'minor', 'adult', 'adresse', 'country')



admin.site.register(Contact, ContactAdmin)
admin.site.register(Wizard, WizardAdmin)