from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import Subscribe
from django.contrib.auth.models import User


# Create your views here.


def index(request):
	return render(request,'index.html')


def subLoad(request,id):
	sub = Subscribe.objects.get(id=id)
	sub_list = list(sub.subscriber.values())
	return JsonResponse(sub_list,safe=False,status=200)

def add_sub(request,id):
	subscribers = Subscribe.objects.get(id=id)
	user = request.user
	if user in subscribers.subscriber.all():
		subscribers.subscriber.remove(user)
		response = 'Subscribe'
		return JsonResponse(response,safe=False,status=200)
	else:
		subscribers.subscriber.add(user)
		response = 'Unsubscribe'
		return JsonResponse(response,safe=False,status=200)
