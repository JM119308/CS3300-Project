from django.urls import path
from . import views

urlpatterns = [
path('', views.index, name = 'index'),
path('manager/home', views.manager, name = 'manager'),
path('employees/', views.EmployeeListView.as_view(), name= 'employees'),
path('employees/<int:pk>', views.EmployeeDetailView.as_view(), name='employee-detail'),
path('update_employee/<int:employee_id>/update', views.updateEmployee, name='update_employee'),

#path('prototype/', views.prototype, name = 'prototype'),

path('schedules', views.ScheduleListView.as_view(), name='schedules'),
path('schedules/<int:pk>', views.ScheduleDetailView.as_view(), name='schedule-detail'),
path('week/<int:week_id>/create_schedule', views.createSchedule, name='create_schedule'),
path('delete_schedule/<int:schedule_id>', views.deleteSchedule, name='delete_schedule'),
path('update_schedule/<int:schedule_id>/update', views.updateSchedule, name='update_schedule'),

path('weeks', views.WeekListView.as_view(), name='weeks'),
path('week/<int:pk>', views.WeekDetailView.as_view(), name='week-detail'),
path('week/create_week', views.createWeek, name='create_week'),
path('delete_week/<int:pk>', views.deleteWeek, name='delete_week'),
path('update_week/<int:pk>', views.updateWeek, name='update_week'),

path('availability/<int:pk>', views.AvailabilityDetailView.as_view(), name='availability-detail'),
path('availability/<int:employee_id>/update/', views.updateAvailability, name='update_availability'),


path('accounts/register/', views.registerPage, name = 'register_page'), 
path('user/', views.userPage, name = 'user_page'),

]
