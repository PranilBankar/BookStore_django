from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('add/<int:book_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='view_cart'),
]
