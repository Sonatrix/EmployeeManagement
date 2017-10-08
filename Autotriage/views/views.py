from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.

def home(request):
    return render(request, 
        'autotriage/dashboard.html', 
        {
            
        }
    )
