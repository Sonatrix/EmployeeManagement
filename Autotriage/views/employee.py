from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from Autotriage.forms import AddEmployeeForm

def employeeList(request):
    return render(request,
                  'autotriage/employee/employee_list.html',
                  {

                  }
                  )

def addEmployee(request):
     # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AddEmployeeForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/employee_list')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AddEmployeeForm()

    return render(request, 'autotriage/employee/add_employee.html', {'form': form})
