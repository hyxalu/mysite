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
    path('contact_success/', views.contact_success, name='contact_success'),
    path('who/', views.who, name='who'),
    path('login/', auth_views.LoginView.as_view(template_name='umm/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('email_members/', views.email_members, name='email_members'),
    path('email_members_success/', views.email_members_success, name='email_members_success'),
    path('password_reset/', auth_views.PasswordResetView.as_view(success_url='../password_reset_done/', template_name='umm/password_reset.html', email_template_name='umm/password_reset_email.txt'), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='umm/password_reset_done.html'), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(success_url='../../../password_reset_complete', template_name='umm/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='umm/password_reset_complete.html'), name='password_reset_complete')
]
