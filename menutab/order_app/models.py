# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User, Group
from django.conf import settings
from datetime import datetime
# Create your models here.
MENU_STATUS = ((0, '대기'), (1, '진행'), (2, '완료'), (3, '취소'))

class OrderManager(models.Manager):
	def create_order(self, userid,menu_name,count,row,table_code, device_key, **extra_fields):   
		if not menu_name:
			raise ValueError('The given menu_name must be set')
		user = User.objects.get(id = userid)
		order = self.model(user=user, menu_name = menu_name,table_code = table_code,device_key = device_key, **extra_fields)
		print order
		order.save(using=self._db)
		return order

	def update_order(self,id, user,menu_name,count,row,table_code, device_key, status,**extra_fields):
		"""
		Order 업데이트
		"""
		# u = User.objects.get(username = username)  
		order = Order.objects.get(id=id)
		user = User.objects.get(id = user) 
		if not order:
		    raise ValueError('The given game must be set')
		# profile.user = u
		order.menu_name = name
		order.device_key = device_key
		order.row = row
		order.count = count
		order.table_code = table_code
		order.user = user
		order.status = status

		print order
		order.save(using=self._db)
		return order


class Order(models.Model):
	user = models.ForeignKey(User)
	menu_name = models.CharField(max_length=255)
	count = models.IntegerField(default=1);
	row = models.CharField(max_length=255)
	table_code = models.CharField(max_length=255)
	device_key = models.CharField(max_length=255)
	status = models.IntegerField(choices=MENU_STATUS, default=0)
	order_time = models.DateTimeField(auto_now_add=True)
	objects = OrderManager()

	def serialize(self):
		data = {
            'id':self.id,
            'user':self.user_id,
            'menu_name':self.menu_name,
            'count':self.count,
            'row':self.row,
            'table_code':self.table_code,
            'device_key':self.device_key,
            'status':self.status,
            'order_time':self.order_time.ctime()
        }
        	return data
	class Meta:
		verbose_name = u'Order'
		verbose_name_plural = u'Order'
	def __unicode__(self):
		return self.menu_name
		# return  u'테이블'+ self.table_code + u'메뉴'+ self.menu_name  +':'+ self.time.__str__()




