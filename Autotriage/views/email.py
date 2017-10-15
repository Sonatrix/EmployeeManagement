from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from Autotriage.forms import EmailForm
from Autotriage.models import Email


@login_required
def emailList(request):
    emails = Email.objects.all()
    return render(request,
                  'autotriage/email/email_list.html',
                  {
                      'emails': emails
                  }
                  )


@login_required
def addEmail(request):
     # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = EmailForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/email/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = EmailForm()

    return render(request, 'autotriage/email/add_email.html', {'form': form})


def emailDetail(request,id):

    email = Email.objects.get(id=id)
    return render(request, 'autotriage/email/email_details.html', {'email': email, 'id': id})


@login_required
def deleteEmail(request,id):

    email = Email.objects.get(id=id)
    if email:
        email.delete()
    return HttpResponseRedirect('/email/')


@login_required
def editEmail(request, id):
     # if this is a POST request we need to process the form data
    email = Email.objects.get(id=id)
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = EmailForm(request.POST, instance=email)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/email/detail/' + str(id))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = EmailForm(instance=email)

    return render(request, 'autotriage/email/edit_email.html', {'form': form, 'id': id})
