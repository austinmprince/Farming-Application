from django.urls import path, include

from . import views
app_name = 'veg_app'
urlpatterns = [
    # serves up views.home function in views
    # in this folder

    path('', views.home, name='csa-home'),
    path('farmers/', include(([
        path('main/', views.farmer_main, name='farmer-home'),

    ], 'veg_app'), namespace='farmers')),
    path('consumers/', include(([
        path('main/', views.consumer_main, name='consumer-home'),
    ], 'veg_app'), namespace='consumers')),

    path('about/', views.about, name='csa-about'),



]
