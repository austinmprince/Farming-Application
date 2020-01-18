from django.urls import path

from .views import veg_app
app_name = 'veg_app'
urlpatterns = [
    # serves up views.home function in views
    # in this folder
    path('', veg_app.home, name='csa-home'),
    path('about/', veg_app.about, name='csa-about'),



]
