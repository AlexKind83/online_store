from django.urls import path, include
from . import views

urlpatterns = [

    path('', include('django.contrib.auth.urls')),  # обращение к django url-адресам
    path('main_page/', views.main_page, name='main_page'),
    path('register/', views.register, name='register'),
]
