from django.urls import path

from . import views

app_name= 'store'

urlpatterns = [
    path('', views.product_all, name='all_products'),
        path('search/<slug:category_slug>/', views.category_list, name='category_list'),
        path('<slug:slug>', views.product_detail, name='product_detail'),

]
print('inside views')
