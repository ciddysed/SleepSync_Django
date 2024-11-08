from django.urls import path
from . import views

urlpatterns = [
    path('', views.sleep_schedule_list, name='schedule_list'),
    path('create/', views.sleep_schedule_create, name='schedule_create'),
    path('update/<int:id>/', views.sleep_schedule_update, name='schedule_update'),
    path('delete/<int:id>/', views.sleep_schedule_delete, name='schedule_delete'),
]
