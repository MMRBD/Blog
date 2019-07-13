from django.shortcuts import render, redirect
from .models import PhoneBook
from .forms import PhoneBookForms
from django.contrib import messages


def home(request):
    all_contact = PhoneBook.objects.all
    return render(request, 'phone_book/home.html', {'all_contact': all_contact})


def edit(request, contact_id):
    if request.method == "POST":
        contact_num = PhoneBook.objects.get(pk=contact_id)
        form = PhoneBookForms(request.POST or None, instance=contact_num)
        if form.is_valid():
            form.save()
            messages.success(request, "Contact Edit has been Added!!")
            return redirect('p_home')
        else:
            messages.success(request, "Contact edit fail!!")
            return render(request, 'phone_book/add_contact.html', {})

    else:
        get_contact = PhoneBook.objects.get(pk=contact_id)
        return render(request, 'phone_book/edit.html', {'get_contact': get_contact})


def add_contact(request):
    if request.method == "POST":
        form = PhoneBookForms(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, "Contact has been Added!!")
            return redirect('p_home')
        else:
            messages.success(request, "Contact save fail!!")
            return render(request, 'phone_book/add_contact.html', {})
    else:
        return render(request, 'phone_book/add_contact.html', {})


def delete(request, contact_id):
    if request.method == "POST":
        current_contact = PhoneBook.objects.get(pk=contact_id)
        current_contact.delete()
        messages.success(request, "Contact has been DELETED!!")
        return redirect('p_home')

    else:
        messages.success(request, "Nothing to see here..!!")
        return redirect('p_home')
