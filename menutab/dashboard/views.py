from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login, logout
from menutab.utils import *
from django.utils import simplejson
from pushs.models import MenuTabApp 
from django.shortcuts import render_to_response
from django.template import RequestContext


def serve_html(request, page):
    return render_to_response("dashboard/" +  page + '.html', {}, context_instance=RequestContext(request))

def main_html(request):
    return render_to_response("dashboard/" +  "dashboard" + '.html', {}, context_instance=RequestContext(request))

@need_auth
def login_view(request):
    return toJSON({'status':'ok',
                   'user':request.user.username})
