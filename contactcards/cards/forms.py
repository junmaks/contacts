from django import forms
from .models import ContactCards, PhoneNumberModel


class CardForm(forms.ModelForm):

    class Meta:
        model = ContactCards
        # fields ='__all__' Лучше описать все поля
        fields = ['name', 'surname', 'patronymic', 'date_born', 'employer', 'position', 'address', 'hobbies',
                  'add_info', ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'rows': 1}),
            'surname': forms.TextInput(attrs={'class': 'form-control', 'rows': 1}),
            'patronymic': forms.TextInput(attrs={'class': 'form-control ', 'rows': 1}),
            'date_born': forms.TextInput(attrs={'type': 'date', 'class':'form-control'}),
            'employer': forms.Select(attrs={'class': 'form-control', 'rows': 1}),
            'position': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'hobbies': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'add_info': forms.Textarea(attrs={'class': 'form-control'}),

        }


class PhoneNumberForm(forms.ModelForm):

    class Meta:
        model = PhoneNumberModel
        # fields ='__all__' Лучше описать все поля
        fields = ['phone_number', ]
        widgets = {
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'rows': 1}),

        }



