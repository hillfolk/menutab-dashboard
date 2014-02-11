# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login, logout
from .utils import *
from django.utils import simplejson
from push_app.models import MenuTabApp 
from django.shortcuts import render_to_response
from django.template import RequestContext

def serve_html(request, page):
    return render_to_response('orderboard/' + page + '.html', {}, context_instance=RequestContext(request))

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
		count = 1#data['count']
		row = "1층"#data['row']
		table_code = data['table_code']
		device_key = data['device_key']
		user =  User.objects.get(username = username)

		order = Order.objects.create_order(userid = user.id,menu_name = menu_name,count=count,row=row,table_code = table_code,device_key=device_key);
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

@need_auth
def order_update_view(request,num,method):

	if method == 'update' and request.method == 'POST':
		user =  request.user
		data = json.loads(request.body)
		menu_name =  data['menu_name']
		table_code = data['table_code']
		device_key = data['device_key']
		status = data['status']
		order = Order.objects.get(id=num)
		order.menu_name = menu_name
		order.table_code = table_code
		order.device_key = device_key
		order.status =  status
		Order.objects.order_update(id = data['id'],user = user, menu_code = data['menu_name'],count = data['count'],row = data["row"] ,table_code =data['table_code'],device_key = data['device_key'],status = data['status'])
		return toJSON(order.serialize())
	elif method == 'cookstart' and request.method == 'POST':
		user =  request.user
		order = Order.objects.get(id = num)
		order.status = 1;
		# try:
		# 	device = MenuTabApp.objects.get(dev_id = order.device_key)
		# except MenuTabApp.DoesNotExist:
		# 	device = None
		# 	return toJSON({'status':'None'})
		order.save()
		print order;
		# msg =  order.table_code +u' 테이블에서 주문하신 '+ order.menu_name+u'가 완성되었습니다.'
		# device.send_message(msg)
		return toJSON({'status':'ok'})
	elif method == 'cookdone' and request.method == 'POST':
		user =  request.user
		order = Order.objects.get(id = num)
		order.status = 2;
		# try:
		# 	device = MenuTabApp.objects.get(dev_id = order.device_key)
		# except MenuTabApp.DoesNotExist:
		# 	device = None
		# 	return toJSON({'status':'None'})
		order.save()
		print order;
		msg =  order.table_code +u' 테이블에서 주문하신 '+ order.menu_name+u'가 완성되었습니다.'
		# device.send_message(msg)
		return toJSON({'status':'ok'})
	else:
		return HttpResponse('bad request',status=400)


	


@need_auth
def login_view(request):
    return toJSON({'status':'ok',
                   'user':request.user.username})





