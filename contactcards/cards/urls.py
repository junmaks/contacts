from django.urls import path
from cards.views import *


urlpatterns = [
    path('', index, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('contact/newcontact/', add_contact, name='add_contact'),
    path('contact/<int:contact_id>', info_contact, name='info_contact'),
    path('contact/<int:contact_id>/edit/', edit_contact, name='edit_contact'),

]