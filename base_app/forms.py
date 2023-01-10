from django.contrib.auth import get_user_model
# from django.contrib.auth.models import Group
from django import forms
from .models import SCALE_CHOICES, Expenses, Income, ANIMAL_CHOICES

class SignupForm(forms.ModelForm):
    farmerScale = forms.ChoiceField(choices = SCALE_CHOICES)
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name',"farmerScale"]

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.farmerScale = self.cleaned_data['farmerScale']
        user.save()


class AnimalForm(forms.Form):
    animal = forms.ChoiceField(choices=ANIMAL_CHOICES, widget=forms.Select(attrs={'class':'input-field'}))
    price_per_one = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'input-field'}))
    quantity = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'input-field'}))
    age_week = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'input-field little-field'}))
    age_day = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'input-field little-field'}))

#  ChoiceField(**kwargs)¶

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expenses
        exclude = ["owner_id"]
        fields = "__all__"



class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        exclude = ["owner_id"]
        fields = "__all__"


class AnimalMonthlyForm(forms.Form):
    date = forms.DateField(widget= forms.DateInput(attrs={'type': 'date'}))



class DeathForm(forms.Form):
    animal = forms.ChoiceField(choices=ANIMAL_CHOICES)
    age_week = forms.IntegerField()
    age_day = forms.IntegerField()



class QuantityForm(forms.Form):
    quantity = forms.IntegerField()
