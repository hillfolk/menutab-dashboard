# -*- coding:utf-8 -*-
import json
import base64
from django.contrib.auth import authenticate, login, logout
from orders.models import *
from django.http import HttpResponse
from django_sockjs_server.lib.client import SockJsServerClient



def need_auth(functor):
    def try_auth(request, *args, **kwargs):
        if'HTTP_AUTHORIZATION' in request.META:
            basicauth = request.META['HTTP_AUTHORIZATION']
            user = None
            try:
                b64key = basicauth.split(' ')[1]
                key = base64.decodestring(b64key)
                (username, pw) = key.split(':')
                user = authenticate(username=username, password=pw)
            except:
                pass
            if user is not None:
                login(request, user)
                request.META['user'] = user
                return functor(request, *args, **kwargs)
        logout(request)
        response = HttpResponse()
        response.status_code = 401
        response['WWW-Authenticate'] = 'Basic realm= "Markmedia Menutab Service"'
        return response
    return try_auth


def toJSON(objs, status=200):
    json_str = json.dumps(objs, ensure_ascii=False)
    return HttpResponse(json_str, status=status, content_type='application/json; charset=utf-8')

def serialize(objs):
    return map(lambda x: x.serialize(), objs)

def send_message(message):
    """
    큐 메시지 전송
    """
    a = SockJsServerClient()
    a.publish_message(message)

    return 'send' 
