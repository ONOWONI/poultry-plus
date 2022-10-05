from django.urls import path
from .views import payment_response

urlpatterns = [
    path('callback', payment_response, name='payment_response')
]