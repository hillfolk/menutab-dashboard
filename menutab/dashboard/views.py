# -*- coding:utf-8 -*-
import json
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from menutab.utils import *
from pushs.models import MenuTabApp 
from django.shortcuts import render_to_response
from django.template import RequestContext
from orders.models import Order
from staffcall.models import StaffCall
from datetime import datetime, timedelta
from menutab.settings import *


def redirict_main_page(request):
        """
	redirict_page 페이지 호출 
	"""
        return redirect('/')

@login_required(login_url='/account/login/')
def orderboard_page(request):
	"""
	orderboard 페이지 호출 
	"""
        user = request.user
	return render_to_response('dashboard/orderboard.html', {"username":user.username}, context_instance=RequestContext(request))

@login_required(login_url='/account/login/')
def finishboard_page(request):
	"""
	finishboard 페이지 호출 
	"""
        user = request.user
	return render_to_response('dashboard/finishboard.html', {"username":user.username}, context_instance=RequestContext(request))

@login_required(login_url='/account/login/')
def cancleboard_page(request):
	"""
	cancleboard 페이지 호출 
	"""
        user = request.user
	return render_to_response('dashboard/cancleboard.html',  {"username":user.username}, context_instance=RequestContext(request))

@login_required(login_url='/account/login/')
def finishhistory_page(request):
	"""
	finishhistory 페이지 호출 
	"""
        user = request.user
	return render_to_response('dashboard/finishhistory.html',  {"username":user.username}, context_instance=RequestContext(request))




@login_required(login_url='/account/login/')
def login_view(request):
    return toJSON({'status':'ok',
                   'user':request.user.username})

@login_required(login_url='/account/login/')
def orderboard_view(request):
	"""
	접수된 주문 목록을 제공
	"""
	print request.body
	user =  request.user
	now = datetime.now()
	daysthree_day_ago = now - timedelta(days=3)
	staffcall_list = StaffCall.objects.filter(user__exact=user,status__in = [0]).filter(staffcall_time__range=(daysthree_day_ago, now)).order_by('staffcall_time').all()
	order_list = Order.objects.filter(user__exact=user,status__in = [1]).filter(order_time__range=(daysthree_day_ago, now)).order_by('-order_time').all()

	resp = {
           'order_list' : serialize(order_list),
			}

	return toJSON(resp)


@login_required(login_url='/account/login/')
def cancleboard_view(request):
	"""
	최소된 주문에 대한 목록을 제공한다.

	"""
	user =  request.user
	now = datetime.now()# <3 
	daysthree_day_ago = now - timedelta(days=3)

	# staffcall_list = StaffCall.objects.filter(user__exact=user,status__in = [0]).filter(staffcall_time__range=(daysthree_day_ago, now)).order_by('staffcall_time').all()
	cancle_list = Order.objects.filter(user__exact=user,status__in = [0]).filter(order_time__range=(daysthree_day_ago, now)).order_by('-order_time').all()

	resp = {
           'cancle_list' : serialize(cancle_list)
			}

	return toJSON(resp)


@login_required(login_url='/account/login/')
def finishboard_view(request):
	"""
	완료된 주문 리스트 제공
	"""
	user =  request.user
	now = datetime.now()
	daysthree_day_ago = now - timedelta(days=3)

	finish_list = Order.objects.filter(user__exact=user,status__in = [4]).filter(order_time__range=(daysthree_day_ago, now)).order_by('-order_time').all()

	resp = {
           'finish_list' : serialize(finish_list),
			}

	return toJSON(resp)






@login_required(login_url='/account/login/')
def history_order_view(request):
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
           'history_list' : serialize(order_list),
			}

	return toJSON(resp)


@login_required(login_url='/account/login/')
def history_cancle_view(request):
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
           'history_list' : serialize(order_list),
			}

	return toJSON(resp)
