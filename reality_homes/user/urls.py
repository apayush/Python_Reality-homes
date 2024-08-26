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
from user import views
from django.contrib.auth import views as auth_views

urlpatterns = [
path('home', views.home, name='home'),
    path('about', views.about, name='about'),
    path('registration', views.registration, name='registration'),
    path('rstore', views.rstore, name='rstore'),
    path('login', views.login, name='login'),
    path('login_check', views.login_check, name='login_check'),
    path('logout', views.logout, name='logout'),
    path('contact', views.contact, name='contact'),
    path('contact_store', views.contact_store, name='contact_store'),
    path('feedback', views.feedback, name='feedback'),
    path('feedback_store', views.feedback_store, name='feedback_store'),
    path('view_profile/', views.view_profile, name='view_profile'),
    path('edit_profile/<int:id>', views.edit_profile, name='edit_profile'),
    path('update_profile/<int:id>', views.update_profile, name='update_profile'),
    path('add_property', views.add_property, name='add_property'),
    path('property_store', views.property_store, name='property_store'),
    path('view_my_property/', views.view_my_property, name='view_my_property'),
    path('view_property_details/<int:id>', views.view_property_details, name='view_property_details'),
    path('add_images/<int:id>', views.add_images, name='add_images'),
    path('add_images_store', views.add_images_store, name='add_images_store'),
    path('search_property', views.search_property, name='search_property'),
    path('search_with_details', views.search_with_details, name='search_with_details'),
    path('view_property/<int:id>', views.view_property, name='view_property'),

    path('request/<int:id>', views.request, name='request'),
    path('request_store', views.request_store, name='request_store'),


    path('view_request', views.view_request, name='view_request'),
    path('view_my_request', views.view_my_request, name='view_my_request'),
    path('accept_request/<int:id>', views.accept_request, name='accept_request'),
    path('accept_request_store/<int:id>', views.accept_request_store, name='accept_request_store'),


    path('all_properties', views.all_properties, name='all_properties'),

    path('change_password', views.change_password, name='change_password'),
    path('change_password_update', views.change_password_update, name='change_password_update'),

]
