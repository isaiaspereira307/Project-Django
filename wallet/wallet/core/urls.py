from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('carteira/', views.carteira, name='carteira'),
    path('investimentos/', views.investimentos, name='investimentos'),
    path('bitcoin/', views.bitcoin, name='bitcoin'),
]
