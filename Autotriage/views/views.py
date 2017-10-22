from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
# Create your views here.


@login_required
def home(request):
    return render(request, 
        'autotriage/dashboard.html', 
        {
            
        }
    )


def handler404(request):
    response = render_to_response('autotriage/404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request):
    response = render_to_response('autotriage/404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response
