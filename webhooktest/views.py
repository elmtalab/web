import json

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, throttle_classes
from rest_framework.throttling import UserRateThrottle

from webhooktest.models import CryptoHook


#class OncePerDayUserThrottle(UserRateThrottle):
#    rate = '84600/day'


@csrf_exempt
@api_view(http_method_names=['POST'])
#@throttle_classes([OncePerDayUserThrottle])
def register_webhook(request):
    print(request.body)
    request_json = json.loads(request.body)
    print(request.headers['username'])
    print(request_json)
    user = User.objects.get(username=request_json['username'])
    print(user)
    hook = CryptoHook(user=user,
                       event=request_json['event'],
                       target=request_json['callback_url'], crypto_address=request_json['watch_address'])
    # hook.save()  # creates the hook and stores it for later...
    return HttpResponse(hook.crypto_address)





from rest_framework.views import APIView
from rest_framework.response import Response

class HelloView(APIView):
    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)
    def post(self,request):
        print(json.loads(request.body)['username'])
        return Response(request.body)