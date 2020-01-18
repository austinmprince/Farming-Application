from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import FarmerRegisterForm, ConsumerRegisterForm
from django.contrib.auth import authenticate, login
# UserRegisterForm, UserUpdateForm, ProfileUpdateForm, ProfileRegisterForm,
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

class ConsumerSignUpView(CreateView):
    model = CustomUser
    form_class = ConsumerRegisterForm
    template_name = 'users/register_user.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'consumer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('csa-home')


def register(request):
    return render(request, 'users/register.html')
#
# def register_user(request):
#     if request.method == 'POST':
#         form = UserRegisterForm(request.POST)
#         p_form = ProfileRegisterForm(request.POST)
#         if form.is_valid() and p_form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Your account has been created. You may now login')
#             return redirect('login')
#
#     else:
#         form = UserRegisterForm()
#         p_form = ProfileRegisterForm()
#
#     return render(request, 'users/register_user.html', {'form': form, 'p_form':p_form})
#
#
#
# @login_required
# def profile(request):
#     if request.method == "POST":
#         u_form = UserUpdateForm(request.POST, instance=request.user)
#         p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
#         if u_form.is_valid() and p_form.is_valid():
#             u_form.save()
#             p_form.save()
#             messages.success(request, f'Your account has been succesfully updated.')
#             return redirect('profile')
#
#     else:
#         u_form = UserUpdateForm(instance=request.user)
#         p_form = ProfileUpdateForm(instance=request.user.profile)
#
#     context = {
#         'u_form': u_form,
#         'p_form': p_form,
#     }
#
#     return render(request, 'users/profile.html', context)
