from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect


def login_page(request):
    return render(request,'dashboard/login.html')
    

def auth_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return redirect('/orderboard/')
        else:
            return redirect('/')
    else:
        return redirect('/')

def auth_logout(request):
     logout(request)
     return redirect('/account/login/')
    
