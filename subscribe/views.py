from django.shortcuts import render
import os
import math
import random
import requests
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse
from dotenv import load_dotenv
load_dotenv()

#  return redirect(str(process_payment(name,email,amount,phone)))
# Create your views here.
def process_payment(name,email,amount,phone):
    auth_token= os.getenv('FLUTTERWAVE_SECRET_KEY')
    hed = {'Authorization': 'Bearer ' + auth_token}
    data = {
                "tx_ref":''+str(math.floor(1000000 + random.random()*9000000)),
                "amount":amount,
                "currency":"NGN",
                "redirect_url":"http://localhost:8000/callback",
                "payment_plan": 26932,
                "payment_options":"card",
                "meta":{
                    "consumer_id":23,
                    "consumer_mac":"92a3-912ba-1192a"
                },
                "customer":{
                    "email":email,
                    "phonenumber":phone,
                    "name":name
                },
                "customizations":{
                    "title":"Poultry Plus Pro Plan",
                    "description":"Pro version of poultry plus",
                    "logo":"https://getbootstrap.com/docs/4.0/assets/brand/bootstrap-solid.svg"
                }
                }
    url = ' https://api.flutterwave.com/v3/payments'
    response = requests.post(url, json=data, headers=hed)
    response=response.json()
    link=response['data']['link']
    return link




@require_http_methods(['GET', 'POST'])
def payment_response(request):
    status=request.GET.get('status', None)
    tx_ref=request.GET.get('tx_ref', None)
    print(status)
    print(tx_ref)
    return HttpResponse('Finished')
