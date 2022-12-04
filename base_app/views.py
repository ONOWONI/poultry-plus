from django.shortcuts import render, redirect
from subscribe.views import process_payment
from django.contrib.auth.decorators import login_required
from .forms import AnimalForm, ExpenseForm, IncomeForm, AnimalMonthlyForm, DeathForm, QuantityForm
from .models  import Animal, Expenses, Income
from .utils import sumOfArr, age_math
from datetime import datetime, timedelta, date
from django.contrib import messages

def payments_page(request):
    return redirect(str(process_payment()))
    # return redirect(str(process_payment('name','donowoni@gmail.com',100,9133117289)))
    pass


@login_required
# @allowed_users(allowed_users=["pro"]) uncomment when you've finished with pro features
# @cache_page(15)
def home(request):
    print("first",datetime.utcnow())
    # if request.method == 'POST':
    content = {"title": "Dashboard",}
    ## forms
    animal_input_form = AnimalForm(request.POST)
    animal_monthly_form = AnimalMonthlyForm(request.POST)
    ### Database queries
    total_alive_animal = Animal.objects.filter(owner_id = request.user, alive=True).all()
    total_alive_chicken = Animal.objects.filter(owner_id = request.user, alive=True, animal="Chicken").all()
    total_alive_cow = Animal.objects.filter(owner_id = request.user, alive=True, animal="Cow").all()
    total_alive_turkey = Animal.objects.filter(owner_id = request.user, alive=True, animal="Turkey").all()
    total_alive_fish = Animal.objects.filter(owner_id = request.user, alive=True, animal="Fish").all()
    total_alive_goat = Animal.objects.filter(owner_id = request.user, alive=True, animal="Goat").all()
    total_alive_sheep = Animal.objects.filter(owner_id = request.user, alive=True, animal="Sheep").all()
    total_expense = Expenses.objects.filter(owner_id = request.user).all()
    total_income = Income.objects.filter(owner_id = request.user).all()


    # calculations on the queries
    total_animal_quantity = sumOfArr(total_alive_animal,"quantity")
    total_chicken_quantity = sumOfArr(total_alive_chicken,"quantity")
    total_cow_quantity = sumOfArr(total_alive_cow,"quantity")
    total_turkey_quantity = sumOfArr(total_alive_turkey,"quantity")
    total_fish_quantity = sumOfArr(total_alive_fish,"quantity")
    total_goat_quantity = sumOfArr(total_alive_goat,"quantity")
    total_sheep_quantity = sumOfArr(total_alive_sheep,"quantity")
    total_spent = sumOfArr(total_expense, "amount")
    total_earned = sumOfArr(total_income, "amount")
    total_profit = total_earned - total_spent

    ## content
    content["animal_input_form"] = animal_input_form
    content["total_monthly_animal"] = 15
    content["animal_monthly_form"] = animal_monthly_form
    content["total_alive_animal"] = total_animal_quantity
    content["total_alive_chicken"] = total_chicken_quantity
    content["total_alive_cow"] = total_cow_quantity
    content["total_alive_turkey"] = total_turkey_quantity
    content["total_alive_fish"] = total_fish_quantity
    content["total_alive_goat"] = total_goat_quantity
    content["total_alive_sheep"] = total_sheep_quantity
    content["total_money_spent"] = total_spent
    content["total_money_earned"] = total_earned
    content["total_profit"] = total_profit
    if request.method == "POST":
        print("post", datetime.utcnow())
        if animal_input_form.is_valid():
            name = animal_input_form.cleaned_data['animal']
            price_per_one = animal_input_form.cleaned_data['price_per_one']
            quantity = animal_input_form.cleaned_data['quantity']
            age_week = animal_input_form.cleaned_data['age_week']
            age_day = animal_input_form.cleaned_data['age_day']
            age = f"{age_week}.{age_day}"
            user = request.user
            p = Animal(animal=name, price_bought_per_one=price_per_one,quantity=quantity,animal_age_at_bought=float(age),alive=quantity,owner_id=user)
            p.save()
            return redirect(home)
        if animal_monthly_form.is_valid():
            selected_date = animal_monthly_form.cleaned_data['date']

            total_selected_animal = Animal.objects.filter(owner_id = request.user,created_at=selected_date).all()
            selected_alive_animal = Animal.objects.filter(owner_id = request.user,alive=True, created_at=selected_date).all()
            total_expense = Expenses.objects.filter(owner_id = request.user,date=selected_date).all()
            total_income = Income.objects.filter(owner_id = request.user,date=selected_date).all()


            # testing delete soon
            dead_query = Animal.objects.filter(owner_id = request.user,created_at=selected_date, alive=True, animal="Chicken").all()
            print(dead_query)
            for i in dead_query:
                print(i.animal)
            # testing delete soon



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
        print("post end", datetime.utcnow())
    print("last",datetime.utcnow())
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
        'room_name': room_name,
        'owner' : request.user.username
    })


def expenses(request):
    content = {}
    form = ExpenseForm(request.POST)
    if form.is_valid():
        expense = form.save(commit=False)
        expense.owner_id = request.user
        expense.save()
        return redirect("home")
    content["title"] = "Expense"
    content["form"] = form
    return render(request, "views_temp/single_form_template.html", content)


def income(request):
    form= IncomeForm(request.POST)
    if form.is_valid():
        income = form.save(commit=False)
        income.owner_id = request.user
        income.save()
        return redirect("home")
    return render(request, "views_temp/single_form_template.html", {"form": form})


def death_of_a_bird(request):
    context = {}
    form = DeathForm(request.POST)
    if request.method =="POST":
        if form.is_valid():
            animal_form_data = form.cleaned_data['animal']
            age_week_form_data = form.cleaned_data['age_week']
            age_day_form_data = form.cleaned_data['age_day']
            user = request.user.id
            # below is the code to calculate the age of the animal and query it
            age_in_days = age_math(age_week_form_data, age_day_form_data)
            created_at_date = datetime.strptime(str(date.today()), '%Y-%m-%d') - timedelta(days=age_in_days)
            print(timedelta(days=age_in_days))
            print("created at date",created_at_date)
            dead_query = Animal.objects.filter(owner_id = user,created_at=created_at_date, animal=animal_form_data).first()
            if dead_query:
                query_result = dead_query.alive
                context["query_result"] = f"You have {query_result} alive animals this age"
                time = datetime.strftime(created_at_date, '%Y-%m-%d')
                print(time)
                return redirect("death form", time=time, animal=animal_form_data)
            else:
                messages.info(request, "Sorry we could not find your animal")
    context["form"] = form
    context["title"] = "Death of an animal 😢"
    return render(request, "views_temp/dead.html", context)



def update_death_database(request, time,animal):
    context = {}
    print("time: ", time)
    print("animal", animal)
    dead_query = Animal.objects.filter(owner_id=request.user, created_at=time, animal=animal).first()
    query_result = dead_query.alive
    print(query_result)
    form = QuantityForm(request.POST)
    if request.method =="POST":
        if form.is_valid():
            quantity_form_data = form.cleaned_data['quantity']
            if quantity_form_data > query_result:
                # flash must be less than number of alive animal
                messages.info(request, "Must be lower than alive animals")
            else:
                dead_query.alive = query_result - quantity_form_data
                dead_query.save()
                messages.info(request, "Updated")
                return redirect("home")

    context["title"] = "Death of an animal"
    context["query_result"] = f"You have {query_result} alive animals this age"
    context["form"] = form
    return render(request, "views_temp/dead.html", context)


def handle_404_Error(request, exception):
    context = {}
    context["title"] = "404"
    return render(request, "error_pages/404_error_page.html")
