from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from Autotriage.forms import ContactForm
from Autotriage.models import Contact


@login_required
def contactList(request, branch_id):
    contacts = Contact.objects.filter(branch_id=branch_id)
    return render(request,
                  'autotriage/contact/contact_list.html',
                  {
                      'contacts': contacts,
                      'branch_id': branch_id
                  }
                  )


@login_required
def addContact(request, branch_id):
     # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/contact/' + str(branch_id))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactForm()

    return render(request, 'autotriage/contact/add_contact.html', {'form': form,'branch_id':branch_id})


def contactDetail(request, contact_id):

    contact = Contact.objects.get(id=contact_id)
    return render(request, 'autotriage/contact/contact_details.html', {'contact': contact,'contact_id':contact_id})


@login_required
def deleteContact(request, branch_id, contact_id):

    contact = Contact.objects.get(id=contact_id)
    if contact:
        contact.delete()
    return HttpResponseRedirect('/contact/' + str(branch_id))


@login_required
def editContact(request, contact_id):
     # if this is a POST request we need to process the form data
    contact = Contact.objects.get(id=contact_id)
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST, instance=contact)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/contact/detail/' + str(contact_id))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactForm(instance=contact)

    return render(request, 'autotriage/contact/edit_contact.html', {'form': form, 'contact_id': contact_id})
