from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from Autotriage.forms import AddServerForm
from Autotriage.models import CompanyServer


def serverList(request, branch_id):
    
    servers = CompanyServer.objects.filter(branch_id=branch_id)
    return render(request,
                  'autotriage/server/server_list.html',
                  {
                      'servers': servers,
                      'branch_id': branch_id
                  }
                )


def servers(request):

    server = CompanyServer.objects.all()
    return render(request,
                  'autotriage/server/server_list.html',
                  {
                      'servers': server
                  }
                )


@login_required
def addServer(request, branch_id):
     # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AddServerForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/server_list/' + str(branch_id))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AddServerForm()

    return render(request, 'autotriage/server/add_server.html', {'form': form, 'branch_id': branch_id})


@login_required
def addServerDirect(request):
     # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AddServerForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/servers/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AddServerForm()

    return render(request, 'autotriage/server/add_server.html', {'form': form})


def serverDetail(request, server_id):

    server = get_object_or_404(CompanyServer, id=server_id)
    return render(request, 'autotriage/server/server_details.html', {'server': server})


@login_required
def deleteServer(request, pid):

    server = get_object_or_404(CompanyServer, id=pid)
    if server:
        server.delete()
    return HttpResponseRedirect('/server_list/')


@login_required
def editServer(request, pid):
     # if this is a POST request we need to process the form data
    server = get_object_or_404(CompanyServer, id=pid)
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
