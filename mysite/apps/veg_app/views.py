from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404
from .decorators import farmer_required
from django.contrib.auth.decorators import login_required
from ..users.models import Farmer, Consumer, CustomUser


#
# Create your views here.
def home(request):
    if request.user.is_authenticated:
        if request.user.is_farmer:
            # farmer = Farmer.objects.get(user=request.user)
            farmer = Farmer.objects.get(user_id=request.user.id)
            return redirect('veg_app:farmers:farmer-home')
            # return render(request, 'csaApp/farmers/farmer_main.html', {'farmer': farmer})
        elif request.user.is_consumer:
            # consumer = get_object_or_404(Consumer, user_id=request.user.id)
            # return render(request, 'csaApp/consumers/consumer_main.html', {'consumer': consumer})
            return redirect('veg_app:consumers:consumer-home')

    return render(request, 'csaApp/home.html')

def about(request):
    return render(request, 'csaApp/about.html')


def consumer_main(request):
    consumer = get_object_or_404(Consumer, user_id=request.user.id)
    return render(request, 'csaApp/consumers/consumer_main.html', {'consumer': consumer})

def farmer_main(request):
    farmer = get_object_or_404(Farmer, user_id=request.user.id)
    # farmer = Farmer.objects.get(user_id=request.user.id)
    print(farmer)
    return render(request, 'csaApp/farmers/farmer_main.html', {'farmer': farmer})
