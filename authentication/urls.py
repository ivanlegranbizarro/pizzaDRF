from django.urls import path
from . import views

app_name = 'authentication'

urlpatterns = [
    path('', views.UserList.as_view(), name='user-list'),
    path('<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    path('register/', views.UserRegister.as_view(), name='user-register'),
]
