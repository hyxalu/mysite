from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('email/', views.emailView, name='email'),
    path('success/', views.successView, name='success'),
]
