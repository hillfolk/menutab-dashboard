# -*- coding:utf-8 -*-
import json
import time
from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login, logout
from menutab.utils import *
from pushs.models import MenuTabApp
from .models import StaffCall
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import get_object_or_404
from django.utils.log import logging
from datetime import datetime, timedelta


# Create your views here.

logger = logging.getLogger(__name__)

@need_auth
def staffcall_list_view(request):
	"""
	직원호출 리스트 요청
	"""
	user =  request.user
	now = datetime.now() 
	daysthree_day_ago = now - timedelta(days=3)
	staffcall_list = StaffCall.objects.filter(user__exact=user,status__in = [0]).filter(staffcall_time__range=(daysthree_day_ago, now)).order_by('-staffcall_time').all()
	resp = {
           	'staffcall_list' : serialize(staffcall_list)
			}
	return toJSON(resp)

@need_auth
def staffcall_search_view(request):
	"""
	직원호출 검사
	"""
	staffcall_per_page = int(request.GET.get('per_page', 20))
	page_num = int(request.GET.get('page', 1))
	user =  request.user
	staffcall_list = staffcall.objects.filter(user__exact=user,status__in = [0,4]).staffcall_by('-staffcall_time').all()
	pages = Paginator(staffcall_list, staffcall_per_page)
	resp = {
           'total_count' : pages.count,
           'staffcall_list' : serialize(pages.page(page_num).object_list)
			}
	return json.dumps(resp)







def staffcall_create_view(request,method):
	if method == 'create' and request.method == 'POST':
		data = json.loads(request.body)
		username =  data['username']
		staffcall_desc =  data['staffcall_desc']
		count = data['count']
		row = data['row']
		table_code = data['table_code']
		device_key = data['device_key']
		user =  User.objects.get(username = username)

		staffcall = StaffCall.objects.create_staffcall(userid = user.id,staffcall_desc = staffcall_desc,count=count,row=row,table_code = table_code,device_key=device_key);
		message = dict()
		message['channel'] = user.username
		message['data'] = dict()
		message['data']['staffcall'] = staffcall.serialize()
		send_message(message)
		return toJSON (staffcall.serialize())
	else:
		return HttpResponse('bad request',status=400)


def new_staffcall_view(request):
	if request.method == 'POST':
		user =  request.user
		data = json.loads(request.body)
		data[1]
	else:
		return HttpResponse('bad request',status=400)



@need_auth
def staffcall_view(request,num):
	if request.method == 'GET':
		user =  request.user
		staffcall = staffcall.objects.get(id=num)
		return json.dumps(staffcall.serialize())
	else:
		return HttpResponse('bad request',status=400)


def staffcall_update_view(request,num,method):
	if method == 'update' and request.method == 'POST':
		user =  request.user
		data = request.body
		staffcall = get_object_or_404(StaffCall, pk=num)
		beStatus = staffcall.status
		status = request.POST.get('status',staffcall.status)

	
		if status:
			staffcall.status =  status
		if beStatus < staffcall.status:
			if staffcall.status == 0:
				print "접수"
				msg =  staffcall.table_code +u' 테이블에서 요청하신 '+ staffcall.staffcall_desc+u'가 취소되었습니다.'
				# device.send_message(msg)
				print msg
			elif staffcall.status == 1:
				print "완료"
				msg =  staffcall.table_code +u' 테이블에서 요청하신 '+ staffcall.staffcall_desc+u'가 접수되었습니다.'
				#device.send_message(msg)
				print msg

		StaffCall.objects.staffcall_update(id = staffcall.id,user = user.id, staffcall_desc = staffcall.staffcall_desc,count = staffcall.count,row = staffcall.row ,table_code =staffcall.table_code,device_key = staffcall.device_key,status = staffcall.status)
		message = dict()
		message['channel'] = user.username
		message['data'] = dict()
		message['data']['staffcall'] = staffcall.serialize()
		send_message(message)

		return toJSON( staffcall.serialize())
	else:
		return HttpResponse('bad request',status=400)