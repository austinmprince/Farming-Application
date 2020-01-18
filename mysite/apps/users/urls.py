from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    # serves up views.home function in views
    # in this folder
    path('', views.register, name='register'),
    path('user/', views.ConsumerSignUpView.as_view(), name='register-user' ),
    path('farmer/', views.FarmerSignUpView.as_view(), name='register-farmer'),



]
