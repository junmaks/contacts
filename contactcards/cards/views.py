from django.shortcuts import render, get_object_or_404, redirect
from .models import ContactCards, PhoneNumberModel
from .forms import CardForm, PhoneNumberForm


# Create your views here.

def index(request):
    return render(request=request, template_name='cards/index.html', context={})


def contacts(request):
    contacts_all = ContactCards.objects.all()
    print(contacts_all)
    context = {
        "contacts": contacts_all,
        "title": 'All'
    }
    return render(request=request, template_name='cards/contacts.html', context=context)


def info_contact(request, contact_id):
    contact = get_object_or_404(ContactCards, pk=contact_id)  # возвращает 404, если объект модели не найден
    phone_numbers = PhoneNumberModel.objects.filter(id_user=contact_id)
    print(phone_numbers)
    return render(request=request, template_name='cards/information.html', context={'contact': contact,
                                                                                    'phone_numbers': phone_numbers})


def add_contact(request, ):
    if request.method == 'POST':
        form1 = CardForm(request.POST)
        form2 = PhoneNumberForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            print(form1.cleaned_data)
            card = form1.save()
            print(type(card))
            print(card.pk)

            # id_user = card.pk
            phone_number = form2.cleaned_data['phone_number']
            PhoneNumberModel.objects.create(id_user=card, phone_number=phone_number)

            return redirect(card)
    else:
        form1 = CardForm()
        form2 = PhoneNumberForm()
    context = {
        'form1': form1,
        'form2': form2,
    }
    return render(request=request, template_name='cards/add_contact.html', context=context)


def edit_contact(request, contact_id):
    # print(__name__)
    contact = get_object_or_404(ContactCards, pk=contact_id)
    phone = PhoneNumberModel.objects.get(id_user=contact_id)
    # print(contact.name)
    # print(request.method)
    if request.method == 'POST':
        form1 = CardForm(request.POST, instance=contact)
        form2 = PhoneNumberForm(request.POST, instance=phone)
        print(contact.surname)
        if form1.is_valid():
            card = form1.save()
            return redirect(card, pk=contact_id)
    else:
        form1 = CardForm(instance=contact)
        form2 = PhoneNumberForm(instance=phone)
    context = {
        'form1': form1,
        'form2': form2
    }
    return render(request=request, template_name='cards/add_contact.html', context=context)
