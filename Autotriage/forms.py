from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone
from Autotriage.models import Employee , Company, CompanyServer, Branch, Contact, Email


class AddEmployeeForm(UserCreationForm):
    
    class Meta():
        model = Employee
        include = ('username', 
                   'designation', 'email', 'first_name', 'is_staff', 'is_active')
        exclude = ('deleted', 'inserted_by', 'groups', 'password',
                   'profile_pic', 'user_permissions', 'date_joined', 'last_login')


class AddCompanyForm(forms.ModelForm):

    class Meta:
        model = Company
        exclude = ('deleted',)

class AddServerForm(forms.ModelForm):
    
    class Meta:
        model = CompanyServer
        include = ('server_os', 'username', 'password')
        exclude = ('deleted',)

class AddBranchForm(forms.ModelForm):
    
    class Meta:
        model = Branch
        exclude = ('deleted', 'added_date', 'pid')

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ('added_date',)


class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
        exclude = ('added_date',)

