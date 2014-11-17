# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User, Group
from django.conf import settings
from datetime import datetime
# Create your models here.
MENU_STATUS = ((0, '취소'), (1, '대기'), (2, '처리'), (3, '완료'),(4, '수령'))


class OrderManager(models.Manager):

	def create_order(self, userid, menu_name, menu_price,count,option, row, table_code, device_key, **extra_fields):
		"""
		Order 생성
		"""
		if not menu_name:
			raise ValueError('The given menu_name must be set')
		user = User.objects.get(id=userid)
		order = self.model(user=user, menu_name=menu_name,menu_price = menu_price,option = option,
		                   table_code=table_code,count = count,row = row,device_key=device_key, **extra_fields)

		order.save(using=self._db)
		return order

	def order_update(self, id, user, menu_name,option,count, row, table_code, device_key, status, **extra_fields):
		"""
		Order 업데이트
		"""
		# u = User.objects.get(username = username)
		order = Order.objects.get(id=id)
		user = User.objects.get(id=user)
		if not order:
		    raise ValueError('The given game must be set')

		order.menu_name = menu_name
		order.option = option
		order.device_key = device_key
		order.row = row
		order.count = count
		order.table_code = table_code
		order.user = user
		order.status = status
		order.save(using=self._db)
		return order

	def get_new_orders(self,id,user):
		return Order.objects.filter(user__exact=user,pk__gt=id,status__in = [4]).order_by('pk')


class Order(models.Model):
	user = models.ForeignKey(User)
	menu_name = models.CharField(max_length=255)
	menu_price =  models.IntegerField(null=False);
	option = models.CharField(max_length=255, default = "")
	count = models.IntegerField(default=1);
	row = models.CharField(max_length=255)
	table_code = models.CharField(max_length=255)
	device_key = models.CharField(max_length=255)
	status = models.IntegerField(choices=MENU_STATUS, default=1)
	order_time = models.DateTimeField(default=datetime.now)
	status_set_time = models.DateTimeField(auto_now=True ,null=True)
	objects = OrderManager()

	def serialize(self):
		data = {
		'id': self.id,
		'user': self.user_id,
		'menu_name': self.menu_name,
		'menu_price' : self.menu_price,
		'option' : self.option,
		'count': self.count,
		'row': self.row,
		'table_code': self.table_code,
		'device_key': self.device_key,
		'status': self.status,
		'status_set_time':self.status_set_time.strftime("%y-%m-%d %H:%M:%S"),
		'order_time': self.order_time.strftime("%y-%m-%d %H:%M:%S")
		}
		return data
	class Meta:
		verbose_name = u'Order'
		verbose_name_plural = u'Order'
	def __unicode__(self):
		return self.menu_name
		# return  u'테이블'+ self.table_code + u'메뉴'+ self.menu_name  +':'+ self.time.__str__()
