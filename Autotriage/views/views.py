from django.shortcuts import render, render_to_response
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.contrib.auth.decorators import login_required
from django.template import RequestContext

@login_required
def home(request):
    return render(request, 
        'autotriage/dashboard.html', 
        {
            
        }
    )


def handler404(request):
    return render(request, 
            'autotriage/404.html',{}
    )


def handler500(request):
    return render(request,
                  'autotriage/500.html', {}
                  )
