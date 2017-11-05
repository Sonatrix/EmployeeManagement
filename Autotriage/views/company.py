from django.shortcuts import render, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from Autotriage.forms import AddCompanyForm
from Autotriage.models import Company


def companyList(request):
    companies = Company.objects.all()
    return render(request,
                  'autotriage/company/company_list.html',
                  {
                      'companies': companies
                  }
                  )

@login_required
def addCompany(request):
     # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AddCompanyForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/company_list/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AddCompanyForm()

    return render(request, 'autotriage/company/add_company.html', {'form': form})


def companyDetail(request, pid):

    company = get_object_or_404(Company, id=pid)
    return render(request, 'autotriage/company/company_details.html', {'company': company})

@login_required
def deleteCompany(request, pid):

    company = get_object_or_404(Company, id=pid)
    if company:
        company.delete()
    return HttpResponseRedirect('/company_list/')


@login_required
def editCompany(request, pid):
     # if this is a POST request we need to process the form data
    company = get_object_or_404(Company, id=pid)
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AddCompanyForm(request.POST, instance=company)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/company/' + str(company.id))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AddCompanyForm(instance=company)

    return render(request, 'autotriage/company/edit_company.html', {'form': form, 'pid': pid})
