from django.urls import path
from .views import display_data, orders_list_view, ordered_product_list




urlpatterns = [
    path('display-data/', display_data, name='display_data'),
    path('orders/', orders_list_view, name='orders_list'),
    path('ordered-products/', ordered_product_list, name='ordered_product_list')
]