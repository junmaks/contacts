from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.

from .models import ContactCards


class ContactCardsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', )
    list_display_links = ('name', 'surname')
    search_fields = ('name', 'surname')
    list_filter = ('surname',)


admin.site.register(ContactCards, ContactCardsAdmin)
