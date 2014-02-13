# -*- coding:utf-8 -*-
from django.test import TestCase
from .models import *
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.shortcuts import get_list_or_404
import unittest

# Create your tests here.
class orders_test(TestCase):
    def test_index(self):
        resp = self.client.get('/orders/')
        print resp
        self.assertEqual(resp.status_code, 200)


		