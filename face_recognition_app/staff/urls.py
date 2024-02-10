from django.urls import path
from .views import Base_view,LoginView,create_Session,session_view,get_result,model_page

urlpatterns = [
    path('login',LoginView.as_view(),name='login'),
    path('home',Base_view.as_view(),name="home"),
    path('create_session',create_Session,name="create_Session"),
    path('view_session/<str:pk>',session_view,name='session_view'),
    path('get_result/',get_result,name="get_result"),
    path('model_page/',model_page,name="model_Page"),
]