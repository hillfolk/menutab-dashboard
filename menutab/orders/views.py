# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login, logout
from menutab.utils import *
from django.utils import simplejson
from pushs.models import MenuTabApp 
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import get_object_or_404

# Create your views here.

@need_auth
def order_list_view(request):
    order_per_page = int(request.GET.get('per_page', 10))
    page_num = int(request.GET.get('page', 1))
    #Listing
    user =  request.user

    order_list = Order.objects.filter(user__exact=user).order_by('-order_time').all()

    pages = Paginator(order_list, order_per_page)
    resp = {
            'total_count' : pages.count,
            'order_list' : serialize(pages.page(page_num).object_list)
        }
    return toJSON(resp)


def order_create_view(request,method):
	if method == 'create' and request.method == 'POST':
		data = json.loads(request.body)
		username =  data['username']
		menu_name =  data['menu_name']
		count = data['count']
		row = data['row']
		table_code = data['table_code']
		device_key = data['device_key']
		customer_key = data['customer_key']
		user =  User.objects.get(username = username)

		order = Order.objects.create_order(userid = user.id,menu_name = menu_name,count=count,row=row,table_code = table_code,device_key=device_key,customer_key = customer_key);
		return toJSON(order.serialize())
	else:
		return HttpResponse('bad request',status=400)


def new_order_view(request):
	if request.method == 'POST':
		user =  request.user
		data = json.loads(request.body)
		data[1]
	

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

		Order.objects.order_update(id = order.id,user = user.id, menu_name = order.menu_name,customer_key = order.customer_key,count = order.count,row = order.row ,table_code =order.table_code,device_key = order.device_key,status = order.status)

		return toJSON(order.serialize())
	else:
		return HttpResponse('bad request',status=400)

