from django.urls import path
from . import views



urlpatterns = [
    path("", views.home, name="home"),
    path("bye/", views.bye, name="bye"),
    path("pro/", views.upgrade_to_pro, name="Pro"),
    path("forum/", views.forum_room, name="Forum"),
    path("expense/", views.expenses, name="expense"),
    path("income/", views.income, name="expense"),
    path("<str:room_name>/", views.room, name='room'),
    path("payment/", views.payments_page, name="payment page"),
]
