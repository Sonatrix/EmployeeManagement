from django.core.exceptions import ObjectDoesNotExist
from django.utils.six import StringIO
from django import forms
from django.forms import extras
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
from django.utils import timezone

from Autotriage.models import Employee, Company

class AddEmployeeForm(forms.ModelForm):
    
    class Meta:
        model = Employee
        exclude = ('deleted',)


class AddCompanyForm(forms.ModelForm):

    class Meta:
        model = Company
        exclude = ('deleted',)

