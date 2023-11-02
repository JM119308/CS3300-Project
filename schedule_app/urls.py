from django.urls import path
from . import views

urlpatterns = [
path('', views.index, name = 'index'),
path('employees/', views.EmployeeListView.as_view(), name= 'employees'),
path('employees/<int:pk>', views.EmployeeDetailView.as_view(), name='employee-detail'),

path('schedules', views.ScheduleListView.as_view(), name='schedules'),
path('schedules/<int:pk>', views.ScheduleDetailView.as_view(), name='schedule-detail'),
path('availability/<int:pk>', views.AvailabilityDetailView.as_view(), name='availability-detail'),
path('availability/<int:employee_id>/update/', views.updateAvailability, name='update_availability'),
path('availability/<int:employee_id>/create/', views.createAvailability, name='create_availability'),
]
