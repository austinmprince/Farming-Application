"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
# from apps.veg_app import views as veg_views
# from apps.users import views as user_views



urlpatterns = [
    path('', include('apps.veg_app.urls', namespace='veg_app')),
    path('register/', include('apps.users.urls', namespace='register')),
    path('admin/', admin.site.urls),
    # path('register/', user_views.register, name='register'),
    # path('register/user', user_views.ConsumerSignUpView.as_view(), name='register-user'),
    # path('register/farmer', user_views.FarmerSignUpView.as_view(), name='register-farmer'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),

]
