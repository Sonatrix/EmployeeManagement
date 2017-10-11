from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from Autotriage.forms import AddServerForm
from Autotriage.models import CompanyServer


def serverList(request):
    servers = CompanyServer.objects.all()
    return render(request,
                  'autotriage/server/server_list.html',
                  {
                      'servers': servers
                  }
                  )


def addServer(request):
     # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AddServerForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/server_list/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AddServerForm()

    return render(request, 'autotriage/server/add_server.html', {'form': form})


def serverDetail(request, pid):

    server = CompanyServer.objects.get(id=pid)
    return render(request, 'autotriage/server/server_details.html', {'server': server})


def deleteServer(request, pid):

    server = CompanyServer.objects.get(id=pid)
    if server:
        server.delete()
    return HttpResponseRedirect('/server_list/')


def editServer(request, pid):
     # if this is a POST request we need to process the form data
    server = CompanyServer.objects.get(id=pid)
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AddServerForm(request.POST, instance=server)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/server/' + str(server.id))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AddServerForm(instance=server)

    return render(request, 'autotriage/server/edit_server.html', {'form': form, 'pid': pid})
