from django import forms
# from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Farmer, Consumer, CustomUser
from django.db import transaction


class FarmerRegisterForm(UserCreationForm):
    farm_name = forms.CharField(max_length=150)
    # email = forms.EmailField()
    # field_order = ['farm_name', 'username', 'email']
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'email', 'farm_name']


    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_farmer = True
        user.save()
        farmer = Farmer.objects.create(user=user)
        return user



class ConsumerRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'email']

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_consumer = True
        user.save()
        consumer = Consumer.objects.create(user=user)
        return user
# class UserRegisterForm(UserCreationForm):
#     email = forms.EmailField()
#
#     class Meta:
#         model = CustomUser
#         fields = ['username', 'email', 'password1', 'password2']

# class ProfileRegisterForm(forms.ModelForm):
#     first_name = forms.CharField(max_length=50)
#     last_name = forms.CharField(max_length=150)
#     class Meta:
#         model = Profile
#         fields = ['first_name', 'last_name', 'is_farmrep']
#
# class UserUpdateForm(forms.ModelForm):
#     email = forms.EmailField()
#
#     class Meta:
#         model = User
#         fields = ['username', 'email']
#
# class ProfileUpdateForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['first_name', 'last_name', 'pickups_left']
