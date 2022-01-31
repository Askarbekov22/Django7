from unicodedata import name
from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('register/', views.Registration.as_view(), name="registr"),
    path('login/', views.NewLoginView.as_view(), name="login"),
    path('users/', views.UserListView.as_view(), name="user_all"),
]