from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth.models import User

import getpass

# Create your views here.


def homeView(request):
    if request.user.is_authenticated():
        # do nothing
        user = User.objects.get(username=getpass.getuser())
    else:
        username = getpass.getuser()
        user = User.objects.get(username=username)

        # manually set the backend attribute to bypass password as user is logged into pc under username already
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        login(request, user)
    request.session['facility'] = user.associate.facility
    request.session['username'] = getpass.getuser()
    return render(request, 'home/index.html', {'userName': request.session['username'],'facility': request.session['facility']})

def userView(request):
    return render(request, 'templates/home/index.html')


