from django.urls import path
from . import views

urlpatterns = [
    path('products/',views.index,name='index'),
    path('products/<int:pk>/',views.getProduct, name='product'),
    path('categories/', views.categories, name='categories'),
    path('categories/<int:pk>', views.getCategory, name='category'),
    path('categories/<int:pk>/products', views.getCategory, name='categoryProducts'),
]