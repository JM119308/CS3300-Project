from django.urls import path
from . import views

urlpatterns = [
path('', views.index, name = 'index'),
path('', views.manager, name = 'manager'),
path('employees/', views.EmployeeListView.as_view(), name= 'employees'),
path('employees/<int:pk>', views.EmployeeDetailView.as_view(), name='employee-detail'),
path('schedules', views.ScheduleListView.as_view(), name='schedules'),
path('weeks', views.WeekListView.as_view(), name='weeks'),
path('week/<int:pk>', views.WeekDetailView.as_view(), name='week-detail'),
path('schedules/<int:pk>', views.ScheduleDetailView.as_view(), name='schedule-detail'),
path('availability/<int:pk>', views.AvailabilityDetailView.as_view(), name='availability-detail'),
path('availability/<int:employee_id>/update/', views.updateAvailability, name='update_availability'),

]
