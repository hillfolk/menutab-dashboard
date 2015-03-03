# -*- coding:utf-8 -*-
import time;
import json;
from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login, logout
from menutab.utils import *
from pushs.models import MenuTabApp
from django.shortcuts import render_to_response
from django.template import RequestContext
from datetime import datetime, timedelta
from django.shortcuts import get_object_or_404



SLEEP_SECONDS = 5000
# Create your views here.

@need_auth
def order_list_view(request):
	"""
	접수된 주문 목록을 제공
	"""
	user =  request.user
	now = datetime.now()
	daysthree_day_ago = now - timedelta(days=3)

	order_list = Order.objects.filter(user__exact=user,status__in = [1]).filter(order_time__range=(daysthree_day_ago, now)).order_by('-id').all()

	resp = {
           'order_list' : serialize(order_list),
			}
	return toJSON(resp)

@need_auth
def order_search_view(request):
	user =  request.user
	order_per_page = int(request.GET.get('per_page', 20))
	page_num = int(request.GET.get('page', 1))
	order_list = Order.objects.filter(user__exact=user,status__in = [0,4]).order_by('-order_time').all()
	pages = Paginator(order_list, order_per_page)
	resp = {
           'total_count' : pages.count,
           'order_list' : serialize(pages.page(page_num).object_list)
			}
	return toJSON(resp)



@need_auth
def order_list_completed_view(request,method):
	"""
	접수된 주문 목록의 전체를 완료 합니다. 
	"""

	if method == 'allcompleted' and request.method == 'POST':
		user =  request.user
		now = datetime.now()
		daysthree_day_ago = now - timedelta(days=3)
		order_list = Order.objects.filter(user__exact=user,status__in = [1]).filter(order_time__range=(daysthree_day_ago, now)).order_by('-id').all()
		print order_list
		for order in order_list:
			order.status = 4
			Order.objects.order_update(id = order.id,user = user.id, menu_name = order.menu_name,option = order.option,count = order.count,row = order.row ,table_code =order.table_code,device_key = order.device_key,status = order.status)
                        message = dict()
			message['channel'] = user.username
			message['data'] = dict()
			message['data']['order'] = order.serialize()
			send_message(message)
		return HttpResponse('success',status=200)
	else:
		return HttpResponse('bad request',status=400)



@need_auth
def order_list_cancle_view(request,method):
	"""
	접수된 주문 목록의 전체를 취소 합니다. 
	"""
	if method == 'allcancle' and request.method == 'POST':
		user =  request.user
		now = datetime.now()
		daysthree_day_ago = now - timedelta(days=3)

		order_list = Order.objects.filter(user__exact=user,status__in = [1]).filter(order_time__range=(daysthree_day_ago, now)).order_by('-id').all()

		for order in order_list:
			order.status = 0;
			Order.objects.order_update(id = order.id,user = user.id, menu_name = order.menu_name,option = order.option,count = order.count,row = order.row ,table_code =order.table_code,device_key = order.device_key,status = order.status)
                        message = dict()
			message['channel'] = user.username
			message['data'] = dict()
			message['data']['order'] = order.serialize()
			send_message(message)

		return HttpResponse('success',status=200)
	else:
		return HttpResponse('bad request',status=400)




def order_create_view(request,method):
	if method == 'create' and request.method == 'POST':
		data = json.loads(request.body)
		print data
		username =  data['username']
		menu_name =  data['menu_name']
		menu_price =  data['menu_price']
		option = data['option']
		count = data['count']
		row = data['row']
		table_code = data['table_code']
		device_key = data['device_key']
		user =  User.objects.get(username = username)
		order = Order.objects.create_order(userid = user.id,menu_name = menu_name,option = option,menu_price = menu_price,count=count,row=row,table_code = table_code,device_key=device_key);
		message = dict()
		message['channel'] = user.username
		message['data'] = dict()
		message['data']['order'] = order.serialize()
		send_message(message)
		return toJSON(order.serialize())
	else:
		return HttpResponse('bad request',status=400)

def order_list_create_view(request,method):
	if method == 'createlist' and request.method == 'POST':
		data = json.loads(request.body)
		print data
		username =  data['username']
		table_code = data['table_code']
		device_key = data['device_key']
		row = data['row']
		user =  User.objects.get(username = username)
		cartvos = data['cartvos']
		for cart in cartvos:
			menu_name =  cart['menu_name']
			menu_price =  cart['menu_price']
			option = cart['option']
			count = cart['count']
			order = Order.objects.create_order(userid = user.id,menu_name = menu_name,option = option,menu_price = menu_price,count=count,row=row,table_code = table_code,device_key=device_key)
			message = dict()
			message['channel'] = user.username
			message['data'] = dict()
			message['data']['order'] = order.serialize()
			send_message(message)
		return toJSON(order.serialize())
	else:
		return HttpResponse('bad request',status=400)






@need_auth
def order_view(request,num):
	if request.method == 'GET':
		user =  request.user
		order = Order.objects.get(id=num)
		return toJSON(order.serialize())
	else:
		return HttpResponse('bad request',status=400)

@need_auth
def order_update_view(request,num,method):
	if method == 'update' and request.method == 'POST':

		user =  request.user
		data = request.body
		order = get_object_or_404(Order, pk=num)
		beStatus = order.status
		status = request.POST.get('status',order.status)


		if status:
			order.status =  status
		if beStatus < order.status:
			if order.status == 0:
				print "취소"
				msg =  order.table_code +u' 테이블에서 주문하신 '+ order.menu_name+u'가 취소되었습니다.'
				# device.send_message(msg)
				print msg
			elif order.status == 1:
				print "대기"
				msg =  order.table_code +u' 테이블에서 주문하신 '+ order.menu_name+u'가 접수되었습니다.'
				#device.send_message(msg)
				print msg
			elif order.status == 2:
				print "처리"
				msg =  order.table_code +u' 테이블에서 주문하신 '+ order.menu_name+u'가 조리중입니다.'
				#device.send_message(msg)
				print msg
			elif order.status == 3:
				print "완료"
				msg =  order.table_code +u' 테이블에서 주문하신 '+ order.menu_name+u'가 완료되었습니다.'
				#device.send_message(msg)
				print msg
			elif order.status == 4:
				print "수령"
				msg =  order.table_code +u' 테이블에서 주문하신 '+ order.menu_name+u'가 수되었습니다.'
				#device.send_message(msg)
				print msg



		Order.objects.order_update(id = order.id,user = user.id, menu_name = order.menu_name,option = order.option,count = order.count,row = order.row ,table_code =order.table_code,device_key = order.device_key,status = order.status)

		message = dict()
		message['channel'] = user.username
		message['data'] = dict()
		message['data']['order'] = order.serialize()
		send_message(message)
		return toJSON(order.serialize())
	else:
		return HttpResponse('bad request',status=400)
