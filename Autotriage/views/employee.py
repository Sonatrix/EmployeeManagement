from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from Autotriage.forms import AddEmployeeForm
from Autotriage.models import Employee

def employeeList(request):
    employees = Employee.objects.all()
    return render(request,
            'autotriage/employee/employee_list.html',
                {
                    'employees': employees
                }
            )

def addEmployee(request):
     # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AddEmployeeForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/employee_list/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AddEmployeeForm()

    return render(request, 'autotriage/employee/add_employee.html', {'form': form})

def employeeDetail(request, employee_id):
    
    employee = Employee.objects.get(id=employee_id)
    return render(request, 'autotriage/employee/employee_details.html', {'employee': employee})

def deleteEmployee(request, employee_id):
    
    employee = Employee.objects.get(id=employee_id)
    if employee:
        employee.delete()
    return HttpResponseRedirect('/employee_list/')


def editEmployee(request, employee_id):
     # if this is a POST request we need to process the form data
    employee = Employee.objects.get(id=employee_id)
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AddEmployeeForm(request.POST, instance = employee)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/employee/'+str(employee.id))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AddEmployeeForm(instance = employee)

    return render(request, 'autotriage/employee/edit_employee.html', {'form': form, 'employee_id':employee_id})

    
