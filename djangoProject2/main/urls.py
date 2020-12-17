from django.urls import path
from . import views

urlpatterns = (
    path('', views.index, name='index'),
    path('about-us', views.about, name='about'),
    path('login', views.login, name='login'),
    path('registration', views.register, name='register'),
    path('uni', views.uni, name='uni'),
    path('show', views.show, name='show'),
    path('edit/<str:name>', views.edit, name='edit'),
    path('update/<str:name>', views.update, name='update'),
    path('delete/<str:name>', views.destroy),

)


