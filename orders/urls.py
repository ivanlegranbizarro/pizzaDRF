from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('', views.OrderList.as_view(), name='order-list'),
    path('<int:pk>/', views.OrderDetail.as_view(), name='order-detail'),
    path('create/', views.OrderCreate.as_view(), name='order-create'),
    path('customer/', views.OrdersByCustomer.as_view(), name='orders-by-customer-id'),
    path('customer/<int:pk>/', views.OrdersByCustomerId.as_view(), name='orders-by-customer'),
]
