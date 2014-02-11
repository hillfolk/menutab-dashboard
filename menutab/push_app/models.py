# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User, Group
from django.conf import settings
from datetime import datetime
from gcm.models import AbstractDevice
# Create your models here.

class MenuTabAppManager(models.Manager):

	def update_device(self,id,user,table_code, dev_id,**extra_fields):
		"""
		Order 업데이트
		"""
		# u = User.objects.get(username = username)  
		device = MenuTabApp.objects.get(id=id)
		user = User.objects.get(id = user) 
		if not order:
		    raise ValueError('The given order must be set')
		# profile.user = u
		device.dev_id = dev_id
		device.table_code = table_code
		device.user = user
		device.status = status

		print device
		device.save(using=self._db)
		return device

class MenuTabApp(AbstractDevice):
	user = models.ForeignKey(User,null=True)
	table_code = models.CharField(max_length=200,null=True)
	objects = MenuTabAppManager()

	def serialize(self):
		data = {
            'id':self.id,
            'user':self.user_id,
            'name':self.name,
            'table_code':self.table_code,
            'dev_id':self.dev_id,
            'reg_id':self.reg_id
        }
        	return data
	def __unicode__(self):
		return self.dev_id