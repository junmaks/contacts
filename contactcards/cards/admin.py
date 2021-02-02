from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.

from .models import ContactCards, OrganizationModel, PhoneNumberModel


class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'address',)
    list_display_links = ('name', 'address',)
    search_fields = ('name', 'address',)
    list_filter = ('name',)


class PhoneNumberAdmin(admin.ModelAdmin):
    list_display = ('id_user', 'phone_number', )
    list_display_links = ('id_user', 'phone_number', )
    search_fields = ('id_user', 'phone_number', )
    list_filter = ('id_user', 'phone_number', )


class ContactCardsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', )
    list_display_links = ('name', 'surname')
    search_fields = ('name', 'surname')
    list_filter = ('surname',)


admin.site.register(OrganizationModel, OrganizationAdmin)
admin.site.register(PhoneNumberModel, PhoneNumberAdmin)
admin.site.register(ContactCards, ContactCardsAdmin)
