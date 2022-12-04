from django.urls import path, re_path
from . import views



urlpatterns = [
    path("", views.home, name="home"),
    path("bye/", views.bye, name="bye"),
    path("pro/", views.upgrade_to_pro, name="Pro"),
    path("forum/", views.forum_room, name="Forum"),
    path("expense/", views.expenses, name="expense"),
    path("income/", views.income, name="expense"),
    # path("<str:room_name>/", views.room, name='room'),
    re_path(r"^(?P<room_name>[-\w]+)/$", views.room, name="room"),
    path("payment/", views.payments_page, name="payment page"),
    path("death/no", views.death_of_a_bird, name="dead page"),
    path("deathform/<time>/<str:animal>", views.update_death_database, name="death form")
]


# from django.urls import re_path
# from . import views
# urlpatterns = [
#     re_path(r"^$", views.bye, name="logout"),
# ]