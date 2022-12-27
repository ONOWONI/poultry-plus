import os
import math
import random
import requests
from dotenv import load_dotenv
from .models import TransactionRef
from django.shortcuts import redirect
from django.contrib.auth.models import Group
from django.views.decorators.http import require_http_methods


load_dotenv()

#  return redirect(str(process_payment(name,email,amount,phone)))
# Create your views here.
def process_payment(email, name, user_id):
    auth_token= os.getenv('FLUTTERWAVE_SECRET_KEY')
    hed = {'Authorization': 'Bearer ' + auth_token}
    data = {
            "tx_ref":''+str(math.floor(1000000 + random.random()*9000000)),
            "amount": "5000",
            "currency": "NGN",
            "payment_plan":"28319",
            "redirect_url":"http://localhost:8000/pay/callback",
            "meta": {
                "consumer_id": user_id,
                # "consumer_mac": "92a3-912ba-1192a"
            },
            "customer": {
                "email": email,
                "name": name
            },
            "customizations": {
                "title": "Poultry Plus",
                "description" : "Payment for Poultry plus Premium",
                "logo": "http://www.piedpiper.com/app/themes/joystick-v27/images/logo.png"
            }
        }
    url = "https://api.flutterwave.com/v3/payments"
    response = requests.post(url, json=data, headers=hed)
    response=response.json()
    link=response['data']['link']
    return link




@require_http_methods(['GET', 'POST'])
def payment_response(request):
    status=request.GET.get('status', None)
    tx_ref=request.GET.get('tx_ref', None)
    if status == "successful" :
        paid_group = Group.objects.get(name="Paid")
        request.user.groups.add(paid_group)
        TransactionRef(tr_ref = tx_ref, owner_id=request.user.id)
        return redirect("dashboard")
    else:
        print("Transaction not processed. Please try again")
        return redirect("home")



