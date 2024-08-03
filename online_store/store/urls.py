from django.urls import path
from . import views


app_name = 'store'

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('product_list', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list, name='category_slug'),
    path('<int:pk>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('site_info', views.site_info, name='site_info'),
]


