"""reality_homes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from myadmin import views

urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('', views.login, name='login'),
    path('login_check', views.login_check, name='login_check'),
    path('logout', views.logout, name='logout'),
    path('view_customers', views.view_customers, name='view_customers'),
    path('customer/<int:id>', views.customer, name='customer'),
    path('view_feedback', views.view_feedback, name='view_feedback'),
    path('view_inquiry', views.view_inquiry, name='view_inquiry'),
    path('add_city', views.add_city, name='add_city'),
    path('city_store', views.city_store, name='city_store'),
    path('add_area', views.add_area, name='add_area'),
    path('area_store', views.area_store, name='area_store'),
    path('all_cities', views.all_cities, name='all_cities'),
    path('delete_city/<int:id>', views.delete_city, name='delete_city'),
    path('edit_city/<int:id>', views.edit_city, name='edit_city'),
    path('update_city/<int:id>', views.update_city, name='update_city'),

    path('all_areas', views.all_areas, name='all_areas'),
    path('delete_area/<int:id>', views.delete_area, name='delete_area'),
    path('edit_area/<int:id>', views.edit_area, name='edit_area'),
    path('update_area/<int:id>', views.update_area, name='update_area'),

]
