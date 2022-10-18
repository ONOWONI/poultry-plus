from django.shortcuts import render, redirect
from subscribe.views import process_payment
from django.contrib.auth.decorators import login_required
from .forms import AnimalForm, ExpenseForm, IncomeForm, AnimalMonthlyForm
from .models  import Animal, Expenses, Income
from .utils import sumOfArr


def payments_page(request):
    return redirect(str(process_payment()))
    # return redirect(str(process_payment('name','donowoni@gmail.com',100,9133117289)))
    pass


@login_required
# @allowed_users(allowed_users=["pro"]) uncomment when you've finished with pro features
# @cache_page(15)
def home(request):
    # if request.method == 'POST':
    content = {}
    ## forms
    animal_input_form = AnimalForm(request.POST)
    animal_monthly_form = AnimalMonthlyForm(request.POST)
    ### Database queries
    total_alive_animal = Animal.objects.filter(owner_id = request.user, alive=True).all()
    total_expense = Expenses.objects.filter(owner_id = request.user).all()
    total_income = Income.objects.filter(owner_id = request.user).all()

    # waste of space
    total_animal_quantity = sumOfArr(total_alive_animal,"quantity")
    total_spent = sumOfArr(total_expense, "amount")
    total_earned = sumOfArr(total_income, "amount")
    total_profit = total_earned - total_spent

    ## content
    content["animal_input_form"] = animal_input_form
    content["total_monthly_animal"] = 15
    content["animal_monthly_form"] = animal_monthly_form
    content["total_alive_animal"] = total_animal_quantity
    content["total_money_spent"] = total_spent
    content["total_money_earned"] = total_earned
    content["total_profit"] = total_profit
    if request.method == "POST":
        if animal_input_form.is_valid():
            name = animal_input_form.cleaned_data['animal']
            price_per_one = animal_input_form.cleaned_data['price_per_one']
            quantity = animal_input_form.cleaned_data['quantity']
            age_week = animal_input_form.cleaned_data['age_week']
            age_day = animal_input_form.cleaned_data['age_day']
            age = f"{age_week}.{age_day}"
            user = request.user
            p = Animal(animal=name, price_bought_per_one=price_per_one,quantity=quantity,animal_age=float(age),owner_id=user)
            p.save()
        if animal_monthly_form.is_valid():
            seleted_date = animal_monthly_form.cleaned_data['date']
            total_selected_animal = Animal.objects.filter(owner_id = request.user,created_at=seleted_date).all()
            selected_alive_animal = Animal.objects.filter(owner_id = request.user,alive=True, created_at=seleted_date).all()
            total_expense = Expenses.objects.filter(owner_id = request.user,date=seleted_date).all()
            total_income = Income.objects.filter(owner_id = request.user,date=seleted_date).all()



            total_animal_quantity = sumOfArr(total_selected_animal, "quantity")
            total_selected_alive_animal_quantity = sumOfArr(selected_alive_animal, "quantity")
            total_spent = sumOfArr(total_expense, "amount")
            total_earned = sumOfArr(total_income, "amount")
            total_profit = total_earned - total_spent


            content["total_monthly_animal"] = total_animal_quantity
            content["total_alive_animal"] = total_selected_alive_animal_quantity
            content["total_money_spent"] = total_spent
            content["total_money_earned"] = total_earned
            content["total_profit"] = total_profit
    return render(request, "views_temp/home.html", content)




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


def expenses(request):
    content = {}
    form = ExpenseForm(request.POST)
    if form.is_valid():
        expense = form.save(commit=False)
        expense.owner_id = request.user
        expense.save()
    content["title"] = "Expense"
    content["form"] = form
    return render(request, "views_temp/single_form_template.html", content)


def income(request):
    form= IncomeForm(request.POST)
    if form.is_valid():
        income = form.save(commit=False)
        income.owner_id = request.user
        income.save()
    return render(request, "views_temp/single_form_template.html", {"form": form})
