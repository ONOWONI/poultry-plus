from django.shortcuts import render, redirect
from subscribe.views import process_payment
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from .forms import AnimalForm, ExpenseForm, IncomeForm, AnimalMonthlyForm, DeathForm, QuantityForm
from .models  import Animal, Expenses, Income, ChatModel
from .utils import sumOfArr, age_math
from datetime import datetime, timedelta, date
from django.contrib import messages
from django.db.models import F
from .decorators import allowed_users


User = get_user_model()


def payments_page(request):
    user_email = request.user.email
    user_fname = request.user.first_name
    user_lname = request.user.last_name
    user_id = request.user.id
    user_name = user_fname + " " + user_lname
    return redirect(str(process_payment(user_email, user_name, user_id)))


@login_required
@allowed_users(allowed_users=["Paid"])
# @cache_page(15)
def dashboard(request):
    print("first",datetime.utcnow())
    # if request.method == 'POST':
    content = {"title": "Dashboard",}
    ## forms
    animal_input_form = AnimalForm()
    animal_monthly_form = AnimalMonthlyForm()
    current_user = request.user


    ### Database queries
    total_alive_animal = Animal.objects.filter(owner_id=current_user).all()

    total_alive_animal_dict = {
        "Chicken" : 0,
        "Cow" : 0,
        "Turkey" : 0,
        "Fish" : 0,
        "Goat" : 0,
        "Sheep" : 0,
        "price" : 0.0,
        "dead" : 0
    }
    if total_alive_animal:
        for i in total_alive_animal:
            total_alive_animal_dict[i.name] += i.alive
            total_alive_animal_dict["price"] += i.price_bought_per_one * i.quantity
            if i.alive < i.quantity:
                total_alive_animal_dict["dead"] += (i.quantity - i.alive)




    total_alive_chicken = total_alive_animal_dict["Chicken"]
    total_alive_cow = total_alive_animal_dict["Cow"]
    total_alive_turkey = total_alive_animal_dict["Turkey"]
    total_alive_fish = total_alive_animal_dict["Fish"]
    total_alive_goat = total_alive_animal_dict["Goat"]
    total_alive_sheep =total_alive_animal_dict["Sheep"]
    total_cost_of_animal_bought = total_alive_animal_dict["price"]
    total_dead_animal = total_alive_animal_dict["dead"]
    total_expense = Expenses.objects.filter(owner_id = current_user).all()
    total_income = Income.objects.filter(owner_id = current_user).all()



    # # calculations on the queries
    total_animal_quantity = sumOfArr(total_alive_animal,"alive")
    total_spent = sumOfArr(total_expense, "amount") + total_cost_of_animal_bought
    total_earned = sumOfArr(total_income, "amount")
    total_profit = total_earned - total_spent



    ## content
    content["animal_input_form"] = animal_input_form
    content["animal_monthly_form"] = animal_monthly_form
    content["total_alive_animal"] = total_animal_quantity
    content["total_alive_chicken"] = total_alive_chicken
    content["total_alive_cow"] = total_alive_cow
    content["total_alive_turkey"] = total_alive_turkey
    content["total_alive_fish"] = total_alive_fish
    content["total_alive_goat"] = total_alive_goat
    content["total_alive_sheep"] = total_alive_sheep
    content["total_money_spent"] = float(total_spent)
    content["total_money_earned"] = total_earned
    content["total_profit"] = total_profit
    content["total_dead_animal"] = total_dead_animal

    if request.method == "POST":
        print("post", datetime.utcnow())
        animal_input_form = AnimalForm(request.POST)
        animal_monthly_form = AnimalMonthlyForm(request.POST)
        if animal_input_form.is_valid():
            name = animal_input_form.cleaned_data['animal']
            price_per_one = animal_input_form.cleaned_data['price_per_one']
            quantity = animal_input_form.cleaned_data['quantity']
            age_week = animal_input_form.cleaned_data['age_week']
            age_day = animal_input_form.cleaned_data['age_day']
            age = f"{age_week}.{age_day}"
            p = Animal(name=name, price_bought_per_one=price_per_one,quantity=quantity,animal_age_at_bought=float(age),alive=quantity,owner_id=current_user)
            p.save()
            return redirect(dashboard)
        if animal_monthly_form.is_valid():
            selected_date = animal_monthly_form.cleaned_data['date']


            selected_alive_animal = Animal.objects.filter(owner_id = request.user,alive__gt=0, created_at=selected_date).all()
            total_expense = Expenses.objects.filter(owner_id = request.user,date=selected_date).all()
            total_income = Income.objects.filter(owner_id = request.user,date=selected_date).all()

            selected_alive_animal_dict = {
                "Chicken" : 0,
                "Cow" : 0,
                "Turkey" : 0,
                "Fish" : 0,
                "Goat" : 0,
                "Sheep" : 0,
                "price" : 0,
                "dead" : 0,
            }
            for i in selected_alive_animal:
                selected_alive_animal_dict[i.name] += i.alive
                selected_alive_animal_dict["price"] += (i.price_bought_per_one * i.quantity)
                if i.alive < i.quantity:
                    total_alive_animal_dict["dead"] += (i.quantity - i.alive)



            total_alive_chicken = selected_alive_animal_dict["Chicken"]
            total_alive_cow = selected_alive_animal_dict["Cow"]
            total_alive_turkey = selected_alive_animal_dict["Turkey"]
            total_alive_fish = selected_alive_animal_dict["Fish"]
            total_alive_goat = selected_alive_animal_dict["Goat"]
            total_alive_sheep =selected_alive_animal_dict["Sheep"]
            total_cost_of_animal_bought = selected_alive_animal_dict["price"]
            total_dead_animal = selected_alive_animal_dict["dead"]





            total_selected_alive_animal_quantity = sumOfArr(selected_alive_animal, "alive")
            total_spent = sumOfArr(total_expense, "amount") + total_cost_of_animal_bought
            total_earned = sumOfArr(total_income, "amount")
            total_profit = total_earned - total_spent


            content["total_alive_animal"] = total_selected_alive_animal_quantity
            content["total_alive_chicken"] = total_alive_chicken
            content["total_alive_cow"] = total_alive_cow
            content["total_alive_turkey"] = total_alive_turkey
            content["total_alive_fish"] = total_alive_fish
            content["total_alive_goat"] = total_alive_goat
            content["total_alive_sheep"] = total_alive_sheep
            content["total_money_spent"] = total_spent
            content["total_money_earned"] = total_earned
            content["total_profit"] = total_profit
            content["total_dead_animal"] = total_dead_animal
        else:
            messages.info(request, "Sorry we could not find your animal")
        print("post end", datetime.utcnow())
    print("last",datetime.utcnow())
    return render(request, "views_temp/dashboard.html", content)



@login_required
def upgrade_to_pro(request):
    asdf = Group.objects.filter(user= request.user)
    return render(request, "views_temp/upgradeToPro.html")




def home(request):
    if request.user.is_authenticated:
        return redirect(dashboard)
    context ={}
    context['title'] = "Poultry Plus"
    return render(request, "views_temp/home.html", context)



@login_required
@allowed_users(allowed_users=["Paid"])
def forum_room(request):
    context = {}
    professionals = User.objects.filter(groups__name="PROs")
    context["professionals"] = professionals
    context["title"] = "Forum"
    return render(request, "views_temp/forum.html", context)



@login_required
@allowed_users(allowed_users=["Paid"])
def private_room(request, id):
    context = {}
    other_user_id = User.objects.get(id=id)
    owner = request.user.id

    context['owner'] = request.user.username
    context['other_user_id'] = other_user_id.id
    context["title"] = id

    if owner > other_user_id.id:
        thread_name = f'chat_{owner}-{other_user_id.id}-pro'
    else:
        thread_name = f'chat_{other_user_id.id}-{owner}-pro'

    messages_obj_in_db = ChatModel.objects.filter(thread_name=thread_name)

    context["message"] = messages_obj_in_db

    return render(request, 'views_temp/private_room.html', context)



@login_required
@allowed_users(allowed_users=["Paid"])
def room(request, room_name):
    return render(request, 'views_temp/room.html', {
        'room_name': room_name,
        'owner' : request.user.username,
        "title": room_name
    })



@login_required
@allowed_users(allowed_users=["Paid"])
def expenses(request):
    content = {}
    expenses = Expenses.objects.filter(owner_id = request.user).all().order_by('-date')
    form = ExpenseForm()
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.owner_id = request.user
            expense.save()
            return redirect("expense")
    content["title"] = "Expense"
    content["data"] = expenses
    content["form"] = form
    return render(request, "views_temp/single_form_template.html", content)



@login_required
@allowed_users(allowed_users=["Paid"])
def income(request):
    context = {}
    income_query = Income.objects.filter(owner_id = request.user).all().order_by('-date')
    form= IncomeForm()
    if request.method == "POST":
        form= IncomeForm(request.POST)
        if form.is_valid():
            income = form.save(commit=False)
            income.owner_id = request.user
            income.save()
            return redirect("income")
    context["title"] = "Income"
    context["form"] = form
    context["data"] = income_query
    return render(request, "views_temp/single_form_template.html", context)



@login_required
@allowed_users(allowed_users=["Paid"])
def death_of_a_bird(request):
    context = {}
    total_dead_animal = Animal.objects.filter(owner_id=request.user, alive__lt=F("quantity")).all().order_by("-modified_aat")
    total_dead_animal_array = []
    for i in total_dead_animal:
        array = [i.quantity - i.alive, i.name, i.price_bought_per_one, i.modified_aat]
        total_dead_animal_array.append(array)
    form = DeathForm()
    if request.method =="POST":
        form = DeathForm(request.POST)
        if form.is_valid():
            animal_form_data = form.cleaned_data['animal']
            age_week_form_data = form.cleaned_data['age_week']
            age_day_form_data = form.cleaned_data['age_day']
            user = request.user.id

            # below is the code to calculate the age of the animal and query it
            age_in_days = age_math(age_week_form_data, age_day_form_data)
            created_at_date = datetime.strptime(str(date.today()), '%Y-%m-%d') - timedelta(days=age_in_days)
            dead_query = Animal.objects.filter(owner_id = user,created_at=created_at_date, name=animal_form_data).first()
            if dead_query:
                query_result = dead_query.alive
                context["query_result"] = f"You have {query_result} alive animals this age"
                time = datetime.strftime(created_at_date, '%Y-%m-%d')
                return redirect("death form", time=time, animal=animal_form_data)
            else:
                messages.info(request, "Sorry we could not find your animal")
    context["form"] = form
    context["title"] = "Death of an animal 😢"
    context["dead_data"] = total_dead_animal_array
    return render(request, "views_temp/dead.html", context)



@login_required
@allowed_users(allowed_users=["Paid"])
def update_death_database(request, time,animal):
    context = {}
    user = request.user.id
    form = QuantityForm()
    dead_query = Animal.objects.filter(owner_id=user, created_at=time, name=animal).all()
    index_of_first_non_zero = 0
    for i in dead_query:
        index_of_first_non_zero +=1
        if i.alive > 0 :
            break


    index_of_first_non_zero -=1

    current_dead_query = dead_query[index_of_first_non_zero]
    if request.method =="POST":
        form = QuantityForm(request.POST)
        if form.is_valid():
            quantity_form_data = form.cleaned_data['quantity']
            if quantity_form_data > current_dead_query.alive:
                messages.info(request, "Must be lower than alive animals")
            else:
                current_dead_query.alive -= quantity_form_data
                current_dead_query.save()
                messages.info(request, "Updated")
                return redirect(dashboard)



    context["title"] = "Death of an animal"
    context["query_result"] = f"You have {current_dead_query.alive} alive animals this age"
    context["form"] = form
    return render(request, "views_temp/dead.html", context)


@login_required
def handle_404_Error(request, exception):
    context = {}
    context["title"] = "404"
    return render(request, "error_pages/404_error_page.html")
