from django.core.exceptions import ObjectDoesNotExist
from django.utils.six import StringIO
from django import forms
from django.forms import extras
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
from django.utils import timezone

from Autotriage.models import Employee, Company, CompanyServer, Branch, Contact, Email

class AddEmployeeForm(forms.ModelForm):
    
    class Meta:
        model = Employee
        include = ('username', 'password', 
            'designation','email','first_name', 'is_staff', 'profile_pic')
        exclude = ('deleted', 'inserted_by','groups','profile_pic','user_permissions','date_joined','last_login')


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

