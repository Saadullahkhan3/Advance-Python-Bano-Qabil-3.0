
from django.urls import path, include
from . import views 

urlpatterns = [
    path('total/', views.total, name="total"),
    path('avg/', views.avg, name="avg"),
    path('product/', views.product, name="product"),
]
