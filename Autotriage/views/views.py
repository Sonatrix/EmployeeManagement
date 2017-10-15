from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def home(request):
    return render(request, 
        'autotriage/dashboard.html', 
        {
            
        }
    )
