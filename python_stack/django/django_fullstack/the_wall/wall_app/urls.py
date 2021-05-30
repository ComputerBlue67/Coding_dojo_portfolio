from django.urls import path
from . import views


urlpatterns = [
    path('',views.index),
    path('register', views.register),
    path('login', views.login),
    path('success', views.success),
    path('logout', views.logout),
    path('process_message', views.post_mess),
    path('add_comment/<int:id>',views.post_comment),
]