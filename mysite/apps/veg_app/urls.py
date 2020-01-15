from django.urls import path

from . import views

app_name = 'veg_app'
urlpatterns = [
    # serves up views.home function in views
    # in this folder
    path('', views.home, name='csa-home'),
    path('about/', views.about, name='csa-about'),
    


]
