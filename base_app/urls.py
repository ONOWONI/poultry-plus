from django.urls import path
from . import views



urlpatterns = [
    path("", views.home, name="home"),
    path("bye/", views.bye, name="bye"),
    path("payment/", views.payments_page, name="payment page"),
]
