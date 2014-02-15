# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from .models import MenuTabApp
from django.utils import simplejson
import json
from menutab.utils import *

# Create your views here.


def send_messge(request,id,msg):
	device = MenuTabApp.objects.get(id = id)
	msg =  msg;
	device.send_message(msg)
	return HttpResponse(html);
def order_completed_messge(request,orderid):
	order = Order.objects.get(id = id)
	device = MenuTabApp.objects.get(device_id = device_key)
	msg =  order.table_code +u'테이블에서 주문하신 '+ order.menu_name+u'가 완성되었습니다.'
	device.send_message(msg)
	return HttpResponse(html);

def DeviceBinding(request,method):
	if method == 'binding' and request.method == 'POST':
		data = json.loads(request.body)
		print data
		dev_id =  data['device_id']
		print dev_id
		table_code = data['table_code']
		print table_code

		user = User.objects.get(id = 1)

		device = MenuTabApp.objects.get(dev_id=dev_id)
		device.user = user              
		device.table_code = table_code
		device.save()
		# MenuTabApp.objects.update_device(id=device.id,user = device.user,table_code=table_code,dev_id=dev_id)
# 
		return toJSON(device.serialize())
	else:
		return HttpResponse('bad request',status=400)