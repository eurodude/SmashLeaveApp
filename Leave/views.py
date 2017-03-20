




from django.shortcuts import render
from django.http.request import HttpRequest
#from django.template import RequestContext
from datetime import datetime



def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)

    return render(
        request,
        'basic.html',
        {
            'title':'SMASH - Leave Management Tool',
            'year':datetime.now().year,
        }
    )