# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User, Group
from django.conf import settings
from datetime import datetime
# Create your models here.
STAFFCALL_STATUS = ((0, '호출'),(1, '확인'))


class StaffCallManager(models.Manager):

	def create_staffcall(self, userid, staffcall_desc,count, row, table_code, device_key,customer_key, **extra_fields):
		"""
		StaffCall 생성
		"""
		if not staffcall_desc:
			raise ValueError('The given staffcall_desc must be set')
		user = User.objects.get(id=userid)
		staffcall = self.model(user=user, staffcall_desc=staffcall_desc,
		                   table_code=table_code,count = count,row = row,customer_key = customer_key  ,device_key=device_key, **extra_fields)

		staffcall.save(using=self._db)
		return staffcall

	def staffcall_update(self, id, user, staffcall_desc,count, row, table_code, customer_key,device_key, status, **extra_fields):
		"""
		StaffCall 업데이트
		"""
		# u = User.objects.get(username = username)
		staffcall = StaffCall.objects.get(id=id)
		user = User.objects.get(id=user)
		if not staffcall:
		    raise ValueError('The given game must be set')

		staffcall.staffcall_desc = staffcall_desc
		staffcall.device_key = device_key
		staffcall.row = row
		staffcall.count = count
		staffcall.table_code = table_code
		staffcall.user = user
		staffcall.status = status
		staffcall.customer_key = customer_key
		staffcall.save(using=self._db)
		return staffcall


class StaffCall(models.Model):
	user = models.ForeignKey(User)
	staffcall_desc = models.CharField(max_length=255)
	count = models.IntegerField(default=1);
	row = models.CharField(max_length=255)
	table_code = models.CharField(max_length=255)
	device_key = models.CharField(max_length=255)
	status = models.IntegerField(choices=STAFFCALL_STATUS, default=0)
	customer_key = models.CharField(max_length=255)
	staffcall_time = models.DateTimeField(default=datetime.now)
	status_set_time = models.DateTimeField(auto_now=True ,null=True)
	objects = StaffCallManager()

	def serialize(self):
		data = {
		'id': self.id,
		'user': self.user_id,
		'staffcall_desc': self.staffcall_desc,
		'count': self.count,
		'row': self.row,
		'table_code': self.table_code,
		'device_key': self.device_key,
		'status': self.status,
		'customer_key': self.customer_key,
		'status_set_time':self.status_set_time.strftime("%y-%m-%d %H:%M:%S"),
		'staffcall_time': self.staffcall_time.strftime("%y-%m-%d %H:%M:%S")
		}
		return data
	class Meta:
		verbose_name = u'StaffCall'
		verbose_name_plural = u'StaffCall'
	def __unicode__(self):
		return self.staffcall_desc
		# return  u'테이블'+ self.table_code + u'메뉴'+ self.menu_name  +':'+ self.time.__str__()