from django.shortcuts import render, get_object_or_404, redirect
from .models import ContactCards
from .forms import CardForm


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
    return render(request=request, template_name='cards/information.html', context={'contact': contact})


def add_contact(request, ):
    if request.method == 'POST':
        form = CardForm(request.POST)
        if form.is_valid():
            card = form.save()
            return redirect(card)
    else:
        form = CardForm()
    context = {
        'form': form
    }
    return render(request=request, template_name='cards/add_contact.html', context=context)


def edit_contact(request, contact_id):
    print(__name__)
    contact = get_object_or_404(ContactCards, pk=contact_id)
    print(contact.name)
    print(request.method)
    if request.method == 'POST':
        form = CardForm(request.POST, instance=contact)
        print(contact.surname)
        if form.is_valid():
            card = form.save()
            return redirect(card, pk=contact_id)
    else:
        form = CardForm(instance=contact)
    context = {
        'form': form
    }
    return render(request=request, template_name='cards/add_contact.html', context=context)
