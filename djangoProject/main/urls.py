from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('about-us', views.about, name='about'),
    path('login', views.login, name='login'),
    path('registration', views.register, name='register'),

]
