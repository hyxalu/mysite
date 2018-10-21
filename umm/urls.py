from django.urls import path

from . import views

from django.contrib.auth import views as auth_views

app_name = 'umm'

urlpatterns = [
    path('', views.index, name='index'),
    path('agenda/', views.agenda, name='agenda'),
    path('archives/', views.archives, name='archives'),
    path('detail_event/<int:event_id>', views.detail_event, name='detail_event'),
    path('contact/', views.contact, name='contact'),
    path('success/', views.success, name='success'),
    path('who/', views.who, name='who'),
    path('login/', auth_views.LoginView.as_view(template_name='umm/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('broadcast/', views.broadcast, name='broadcast'),
]
