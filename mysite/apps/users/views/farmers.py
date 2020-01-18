from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth import authenticate, login

from .forms import FarmerRegisterForm, ConsumerRegisterForm
from .models import CustomUser

class FarmerSignUpView(CreateView):
    model = CustomUser
    form_class = FarmerRegisterForm
    template_name = 'users/register_user.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'farmer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('csa-home')
