from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django import forms
from .models import SCALE_CHOICES

class SignupForm(forms.ModelForm):
    farmerScale = forms.ChoiceField(choices = SCALE_CHOICES)
    class Meta:
        model = get_user_model()
        fields = ['first_name',"farmerScale"]

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.farmerScale = self.cleaned_data['farmerScale']
        user.save()
        group = Group.objects.get(name="free")
        user.groups.add(group)
        user.save()



#  ChoiceField(**kwargs)¶