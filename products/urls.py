from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from products import views


urlpatterns = [
    path('products/', views.product_list),
    path('products/available', views.product_list_available),
    path('products/sold', views.product_list_sold),
    path('products/qty', views.product_qty_change),
    path('products/<slug:slug>/', views.product_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
