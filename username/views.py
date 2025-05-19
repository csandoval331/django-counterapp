from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect

from .models import Username
# Create your views here.

def index(request):
    username_list = Username.objects.all()
    ## print(username_list)

    template = loader.get_template('username/index.html')
    context = {'username_list': username_list,'message':'hello from username app in views.py'}
    return HttpResponse(template.render(context, request))

def addusername(request):
    username_obj = Username(username=request.POST['username']).save()
    ## print(username_obj)

    username_list = list(Username.objects.all())

    template = loader.get_template('username/index.html')
    context = {'username_list': username_list,'message':'hello from username app in views.py'}
    return HttpResponse(template.render(context, request))

def removeusername(request, username):
    print(username)
    Username.objects.get(pk=username).delete()

    return HttpResponseRedirect('/username')