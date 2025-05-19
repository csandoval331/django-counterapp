from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Counter
# Create your views here.

def index(request):
    try:
        counter = Counter.objects.get(pk=1)
        print(counter, type(counter), "counter exist")
    except:
        counter = Counter(counter=0, pk=1)
        counter.save()
        print(counter, type(counter), "counter created", )


    template = loader.get_template('counter/index.html')
    context = { "counter":counter }

    return HttpResponse(template.render(context, request))

def down(request):
    counter = Counter.objects.get(pk=1)
    counter.counter = counter.counter - 1
    counter.save()

    return HttpResponseRedirect("/counter")

def up(request):
    counter = Counter.objects.get(pk=1)
    counter.counter = counter.counter + 1
    counter.save()

    return HttpResponseRedirect("/counter")

def reset(request):
    counter = Counter.objects.get(pk=1)
    counter.counter = 0
    counter.save()

    return HttpResponseRedirect("/counter")