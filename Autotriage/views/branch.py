from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from Autotriage.forms import AddBranchForm
from Autotriage.models import Branch


@login_required
def branchList(request, company_id):
    branches = Branch.objects.filter(company_id=company_id)
    return render(request,
                  'autotriage/branch/branch_list.html',
                  {
                      'branches': branches,
                      'company_id': company_id
                  }
            )


@login_required
def addBranch(request, company_id):
     # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AddBranchForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/company/'+str(company_id))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AddBranchForm()

    return render(request, 'autotriage/branch/add_branch.html', {'form': form,'company_id':company_id})


def branchDetail(request, company_id, branch_id):

    branch = Branch.objects.get(id=branch_id)
    return render(request, 'autotriage/branch/branch_details.html', {'branch': branch, 'company_id': company_id})


@login_required
def deleteBranch(request, company_id, branch_id):

    branch = Branch.objects.get(id=branch_id)
    if branch:
        branch.delete()
    return HttpResponseRedirect('/company/'+str(company_id))


@login_required
def editBranch(request, company_id, branch_id):
     # if this is a POST request we need to process the form data
    branch = Branch.objects.get(id=branch_id)
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AddBranchForm(request.POST, instance=branch)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/company/' + str(company_id)+'/detail/'+str(branch_id))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AddBranchForm(instance=branch)

    return render(request, 'autotriage/branch/edit_branch.html', {'form': form, 'company_id': company_id, 'branch_id':branch_id})
