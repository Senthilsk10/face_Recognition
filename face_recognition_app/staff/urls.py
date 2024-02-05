from django.urls import path
from .views import Base_view,LoginView
urlpatterns = [
    path('login',LoginView.as_view(),name='login'),
    path('home',Base_view.as_view(),name="home")
]