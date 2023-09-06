import os
import math
import random
import requests
from dotenv import load_dotenv
from .models import TransactionRef
from django.contrib import messages
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
            # "redirect_url":"https://poultry-plus.onrender.com/pay/callback",
            "redirect_url":"http://localhost:8000/pay/callback",
            "meta": {
                "consumer_id": user_id,
            },
            "customer": {
                "email": email,
                "name": name
            },
            "customizations": {
                "title": "Poultry Plus",
                "description" : "Payment for Poultry plus Premium",
            }
        }
    url = "https://api.flutterwave.com/v3/payments"
    response = requests.post(url, json=data, headers=hed)
    response=response.json()
    link=response['data']['link']
    return link




@require_http_methods(['GET', 'POST'])
def payment_response(request):
    print("0")
    print("0")
    status=request.GET.get('status', None)
    print("0")
    tx_ref=request.GET.get('tx_ref', None)
    print(tx_ref,  " 0")
    if status == "successful" or "cancelled":
        print(status, " 1")
        print(tx_ref)
        paid_group = Group.objects.get(name="Paid")
        print(status, " 2")
        print(tx_ref)
        request.user.groups.add(paid_group)
        print(status , " 3")
        print(tx_ref)
        TransactionRef(tx_ref = tx_ref, owner_id=request.user.id)
        print(status, " 4")
        print(tx_ref)
    # elif status == "cancelled" :
    #     paid_group = Group.objects.get(name="Paid")
    #     request.user.groups.add(paid_group)
    #     TransactionRef(tx_ref = tx_ref, owner_id=request.user.id)
        print(status)
        print(tx_ref)
    else:
        messages.error("Transaction not processed. Please try again")
        return redirect("home")
    return redirect("dashboard")



