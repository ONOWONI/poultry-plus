from django.urls import path, re_path
from . import views



urlpatterns = [
    path("", views.home, name="home"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("pro/", views.upgrade_to_pro, name="Pro"),
    path("forum/", views.forum_room, name="Forum"),
    path("expense/", views.expenses, name="expense"),
    path("income/", views.income, name="income"),
    # path("<str:room_name>/", views.room, name='room'),
    re_path(r"^chat/(?P<room_name>[-\w]+)/$", views.room, name="room"),
    path("personalchat/<int:id>/", views.private_room, name="private room"),
    path("payment/", views.payments_page, name="payment page"),
    path("death/no", views.death_of_a_bird, name="dead page"),
    path("deathform/<time>/<str:animal>", views.update_death_database, name="death form")
]


# from django.urls import re_path
# from . import views
# urlpatterns = [
#     re_path(r"^$", views.bye, name="logout"),
# ]