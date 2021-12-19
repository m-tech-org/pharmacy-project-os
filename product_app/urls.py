from django.urls import path
from django.conf.urls import include
from product_app import views


urlpatterns = [
path('home/<int:product_id>/', views.product_detail, name = 'product_detail'),
path('issue_item/<str:pk>/', views.issue_item, name='issue_item'),   
path('add_to_stock/<str:pk>/', views.add_to_stock, name='add_to_stock'),
path('receipt/', views.receipt, name = 'receipt'),
path('all_sales/', views.all_sales, name = 'all_sales')

]
