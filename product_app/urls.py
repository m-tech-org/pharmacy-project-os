from django.urls import  path
from product_app import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('home/', views.home, name = "home"),
    path('sales_form', views.sales_form, name = "sales_form"),
    path('receipt', views.receipt, name = "receipt"),
    path('update/<int:customer_id>', views.update, name = "update"),
    path('delete/<int:customer_id>', views.delete, name='delete'),
    path('',auth_views.LoginView.as_view(template_name = 'products/login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name = 'products/logout.html'), name='logout'), 
    path('home/<int:product_id>/', views.product_detail, name='product_detail'),
    path('issue_item/<str:pk>/', views.issue_item, name='issue_item'),   
    path('add_item/<str:pk>/', views.add_item, name='add_item')   

]