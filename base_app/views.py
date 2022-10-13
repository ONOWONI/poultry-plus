from django.shortcuts import render, redirect
from subscribe.views import process_payment
from django.contrib.auth.decorators import login_required
from .decorators import allowed_users
from .forms import InventoryForm
from .models  import Inventory


def payments_page(request):
    return redirect(str(process_payment()))
    # return redirect(str(process_payment('name','donowoni@gmail.com',100,9133117289)))
    pass


@login_required
# @allowed_users(allowed_users=["pro"]) uncomment when you've finished with pro features
def home(request):
    # if request.method == 'POST':
    form = InventoryForm(request.POST)
    if request.method == "POST" and form.is_valid():
        name = form.cleaned_data['name']
        price_per_one = form.cleaned_data['price_per_one']
        quantity = form.cleaned_data['quantity']
        age_week = form.cleaned_data['age_week']
        age_day = form.cleaned_data['age_day']
        age = f"{age_week}.{age_day}"
        p = Inventory(name=name, price_bought_per_one=price_per_one,quantity=quantity,animal_age=float(age))
        p.save()
    return render(request, "views_temp/home.html", {"form": form})




def upgrade_to_pro(request):
    return render(request, "views_temp/upgradeToPro.html")


# change later to free page
def bye(request):
    return render(request, "views_temp/bye.html")

def forum_room(request):
    return render(request, "views_temp/forum.html")



def room(request, room_name):
    return render(request, 'views_temp/room.html', {
        'room_name': room_name
    })