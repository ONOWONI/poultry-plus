from urllib import request
from django.shortcuts import render, redirect
from subscribe.views import process_payment
from django.contrib.auth.decorators import login_required


def payments_page(request):
    # return redirect(str(process_payment('name','donowoni@gmail.com',100,9133117289)))
    pass


@login_required
def home(request):
    return render(request, "views_temp/home.html")




def bye(request):
    return render(request, "views_temp/bye.html")