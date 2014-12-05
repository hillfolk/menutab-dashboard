# -*- coding:utf-8 -*-
import time;
import json
from django.shortcuts import render
from django.http import HttpResponse
from .models import MenuTabApp
from datetime import datetime, timedelta
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
		dev_id =  data['device_id']
		table_code = data['table_code']
		userid = data['user_id']
		try:
			user = User.objects.get(username = userid)
		except Exception, e:
			user = User.objects.get(username = "markadmin")

		device = MenuTabApp.objects.get(dev_id=dev_id)
		device.name = userid
		device.user = user   
		device.table_code = table_code
		device.save()
 
		return toJSON(device.serialize())
	else:
		return HttpResponse('bad request',status=400)
