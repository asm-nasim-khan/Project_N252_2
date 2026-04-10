from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("home/",views.Homepage,name='home'),
    path("status_update/",views.StatusUpdate,name='status_update'),
    path("unfriend/<str:friend_email>/",views.Unfriend,name='unfriend'),
    
    
]
