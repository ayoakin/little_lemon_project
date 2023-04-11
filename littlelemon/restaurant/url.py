from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('menu/', views.MenuItemView.as_view()),
    path('menu/<int:pk>/', views.SingleMenuItemView.as_view()),
    path('table/', views.TableItemView.as_view()),
    path('table/<int:pk>/', views.SingleTableItemView.as_view()),
    ]