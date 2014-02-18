from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login, logout
from menutab.utils import *
from django.utils import simplejson
from pushs.models import MenuTabApp 
from django.shortcuts import render_to_response
from django.template import RequestContext
from orders.models import Order
from staffcall.models import StaffCall


def serve_html(request, page):
    return render_to_response("dashboard/" +  page + '.html', {}, context_instance=RequestContext(request))

def main_html(request):
    return render_to_response("dashboard/" +  "dashboard" + '.html', {}, context_instance=RequestContext(request))

@need_auth
def login_view(request):
    return toJSON({'status':'ok',
                   'user':request.user.username})


@need_auth
def dashboard_list_view(request):
	# staffcall_per_page = int(request.GET.get('per_page', 20))
	# page_num = int(request.GET.get('page', 1))
	user =  request.user


	staffcall_list = StaffCall.objects.filter(user__exact=user,status__in = [0]).order_by('-staffcall_time').all()
	wait_list = Order.objects.filter(user__exact=user,status__in = [1]).order_by('-order_time').all()
	process_list = Order.objects.filter(user__exact=user,status__in = [2]).order_by('-order_time').all()
	done_list = Order.objects.filter(user__exact=user,status__in = [3]).order_by('-order_time').all()
	
	resp = {
           'wait_list' : serialize(wait_list),
           'process_list' : serialize(process_list),
           'done_list' : serialize(done_list),
           'staffcall_list' : serialize(staffcall_list)
			}

	return toJSON(resp)
