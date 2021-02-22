from django.urls import path,include
from .import views

urlpatterns = [
    path('', views.Home, name='Home'),
    path('franchise_request',views.franchise_request,name='franchise_request'),
    path('search',views.search,name='search'),
    path('search_result',views.search_result,name='search_result'),
]