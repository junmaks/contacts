from django import forms
from .models import ContactCards


class CardForm(forms.ModelForm):

    class Meta:
        model = ContactCards
        # fields ='__all__' Лучше описать все поля
        fields = ['name', 'surname', 'patronymic', 'date_born', 'phone_number', 'position', 'address', 'hobbies',
                  'add_info', ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'rows': 5}),
            'surname': forms.TextInput(attrs={'class': 'form-control', 'rows': 5}),
            'patronymic': forms.TextInput(attrs={'class': 'form-control ', 'rows': 5}),
            'date_born': forms.TextInput(attrs={'type': 'date', 'class':'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'rows': 5}),
            'position': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'hobbies': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'add_info': forms.Textarea(attrs={'class': 'form-control'}),
        }
