from django.urls import path,re_path
from django.views.generic import TemplateView
from .views import ( 
    RegisterFormView,LoginFormView,LogoutFormView,ContactView)

app_name = 'users'

urlpatterns = [
    path('login/', LoginFormView.as_view() , name='login'),
    path('register/',RegisterFormView.as_view(), name='register'),
    path('logout/' ,LogoutFormView.as_view(), name='logout'),
    # path('contact/',ContactView(),name='contact')
    ]



