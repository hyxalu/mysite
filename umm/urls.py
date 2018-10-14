from django.urls import path

from . import views

app_name = 'umm'

urlpatterns = [
    path('', views.index, name='index'),
    path('agenda/', views.agenda, name='agenda'),
    path('archives/', views.archives, name='archives'),
    path('detail_event/<int:event_id>', views.detail_event, name='detail_event'),
    path('email/', views.email, name='email'),
    path('success/', views.success, name='success'),
    path('who/', views.who, name='who'),
]
