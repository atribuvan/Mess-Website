"""
URL configuration for messwebsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views

urlpatterns = [
    path("", views.home, name="home"),
    path("rules/", views.rules, name="rules"),
    path("caterer/", views.caterer, name="caterer"),
    path("login/", views.login, name="login"),
    path('logout/', views.logout, name='logout'),
    path("links/", views.links, name="links"),
    path("cafeteria/", views.services, name="cafeteria"),
    path("contact/", views.con, name="contact"),
    path("shortRebate/", views.shortRebateForm, name="rebate"),
    path('adminJobs/', views.adminJobs, name='set mess period'),
    path('longRebate/', views.longRebateForm, name='addLongRebateBill'),
    path('profile/', views.profile, name='profile'),
    path('allocationForm/', views.allocationForm, name='allocationForm'),
    path('accept_longrebate/', views.accept_longrebate, name='accept_longrebate'),
    path('edit_caterer/', views.edit_caterer, name='edit_caterer'),
    path('edit_cafeteria/', views.edit_cafeteria, name='edit_cafeteria'),
    path('add_semester/', views.add_semester, name='add_semester'),
    path('add_messperiod/', views.add_messperiod, name='add_messperiod'),
    path('viewShortRebates/', views.viewShortRebates, name='viewRebate'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)