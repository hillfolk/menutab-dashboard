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
from datetime import datetime, timedelta
from menutab.settings import *


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
	user =  request.user
	now = datetime.now()# <3 
	daysthree_day_ago = now - timedelta(days=3)

	staffcall_list = StaffCall.objects.filter(user__exact=user,status__in = [0]).filter(staffcall_time__range=(daysthree_day_ago, now)).order_by('staffcall_time').all()
	order_list = Order.objects.filter(user__exact=user,status__in = [1]).filter(order_time__range=(daysthree_day_ago, now)).order_by('order_time').all()

	resp = {
           'order_list' : serialize(order_list),
           'staffcall_list' : serialize(staffcall_list)
			}

	return toJSON(resp)
@need_auth
def dashboard_search_view(request):
	if request.method == 'POST':
		data = json.loads(request.body)
		user =  request.user
		if not data['ST_value']:
			now = datetime.now()
			months_ago = now - timedelta(days=1)
			order_list = Order.objects.filter(user__exact=user,status__in = [4]).filter(order_time__range=(months_ago, now)).order_by('-order_time').all()
		else:
			start_date = datetime.strptime(data['ST_value'],'%Y/%m/%d')
			end_date =  datetime.strptime(data['ED_value'],'%Y/%m/%d') + timedelta(days=1)
			order_list = Order.objects.filter(user__exact=user,status__in = [4]).filter(order_time__range=(start_date,end_date)).order_by('-order_time').all()
		resp = {
           'order_list' : serialize(order_list),
			}

	return toJSON(resp)

@need_auth
def dashboard_cancle_view(request):
	if request.method == 'POST':
		data = json.loads(request.body)
		user =  request.user
		if not data['ST_value']:
			now = datetime.now()
			months_ago = now - timedelta(days=1)
			order_list = Order.objects.filter(user__exact=user,status__in = [0]).filter(order_time__range=(months_ago, now)).order_by('-order_time').all()
		else:
			start_date = datetime.strptime(data['ST_value'],'%Y/%m/%d')
			end_date =  datetime.strptime(data['ED_value'],'%Y/%m/%d') + timedelta(days=1)
			order_list = Order.objects.filter(user__exact=user,status__in = [0]).filter(order_time__range=(start_date,end_date)).order_by('-order_time').all()
		resp = {
           'order_list' : serialize(order_list),
			}

	return toJSON(resp)
