from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),

    
    path('progress/', views.progress_list, name='progress_list'),
    path('progress/create/', views.progress_create, name='progress_create'),
    path('progress/update/<int:pk>/', views.progress_update, name='progress_update'),
    path('progress/delete/<int:pk>/', views.progress_delete, name='progress_delete'),
    
    path('sleeptrack/', views.sleeptrack_list, name='sleeptrack_list'),
    path('sleeptrack/create/', views.sleeptrack_create, name='sleeptrack_create'),
    path('sleeptrack/update/<int:pk>/', views.sleeptrack_update, name='sleeptrack_update'),
    path('sleeptrack/delete/<int:pk>/', views.sleeptrack_delete, name='sleeptrack_delete'),

    path('users/', views.user_list, name='user_list'),
    path('users/new/', views.user_create, name='user_create'),
    path('users/<int:pk>/edit/', views.user_update, name='user_update'),
    path('users/<int:pk>/delete/', views.user_delete, name='user_delete'),

    path('routines/', views.routine_list, name='routine_list'),
    path('routines/new/', views.routine_create, name='routine_create'),
    path('routines/<int:pk>/edit/', views.routine_update, name='routine_update'),
    path('routines/<int:pk>/delete/', views.routine_delete, name='routine_delete'),

    path('alarms/', views.alarm_list, name='alarm_list'),
    path('alarms/new/', views.alarm_create, name='alarm_create'),
    path('alarms/<int:pk>/edit/', views.alarm_update, name='alarm_update'),
    path('alarms/<int:pk>/delete/', views.alarm_delete, name='alarm_delete'),

    path('', views.landing_page, name='landing_page'),
    path('register/', views.register_view, name='register'),
    path('profile/', views.profile_view, name='profile'),
    path('login/', views.login_view, name='login'), 
    path('logout/', views.logout_view, name='logout'),
    path('sleep_tips/', views.sleep_tips, name='sleep_tips'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('features/', views.features, name='features'),

]
