from django.db import models
from django.urls import reverse
from .times import *

# Create your models here.
	

class Availability(models.Model):

	owner = models.CharField(max_length = 200)
	
	sunday_start = models.CharField(max_length=200, choices=TIMES, blank = True)
	sunday_end = models.CharField(max_length=200, choices=TIMES, blank = True)
	monday_start = models.CharField(max_length=200, choices=TIMES, blank = True)
	monday_end = models.CharField(max_length=200, choices=TIMES, blank = True)
	tuesday_start = models.CharField(max_length=200, choices=TIMES, blank = True)
	tuesday_end = models.CharField(max_length=200, choices=TIMES, blank = True)
	wednesday_start = models.CharField(max_length=200, choices=TIMES, blank = True)
	wednesday_end = models.CharField(max_length=200, choices=TIMES, blank = True)
	thursday_start = models.CharField(max_length=200, choices=TIMES, blank = True)
	thursday_end = models.CharField(max_length=200, choices=TIMES, blank = True)
	friday_start = models.CharField(max_length=200, choices=TIMES, blank = True)
	friday_end = models.CharField(max_length=200, choices=TIMES, blank = True)
	saturday_start = models.CharField(max_length=200, choices=TIMES, blank = True)
	saturday_end = models.CharField(max_length=200, choices=TIMES, blank = True)

	def __str__(self):
		return self.owner
	def get_absolute_url(self):
		return reverse('availability-detail', args=[str(self.id)])

class Employee(models.Model):
	availability = models.ForeignKey(Availability, on_delete=models.CASCADE, default = None)

	STATUS = (
	('Full-Time','Full-time'),
	('Part-Time', 'Part-time')
	)
	name = models.CharField(max_length = 200)
	phone = models.CharField(max_length = 200)
	status = models.CharField(max_length=200, choices=STATUS, blank = True)	


	def __str__(self):
		return self.name
	def get_absolute_url(self):
		return reverse('employee-detail', args=[str(self.id)])	


class Schedule(models.Model):

	employee = models.ForeignKey(Employee, on_delete=models.CASCADE, default = None)

	week = models.CharField(max_length = 200)

	sunday_start = models.CharField(max_length=200, choices=TIMES, blank = True)
	sunday_end = models.CharField(max_length=200, choices=TIMES, blank = True)
	monday_start = models.CharField(max_length=200, choices=TIMES, blank = True)
	monday_end = models.CharField(max_length=200, choices=TIMES, blank = True)
	tuesday_start = models.CharField(max_length=200, choices=TIMES, blank = True)
	tuesday_end = models.CharField(max_length=200, choices=TIMES, blank = True)
	wednesday_start = models.CharField(max_length=200, choices=TIMES, blank = True)
	wednesday_end = models.CharField(max_length=200, choices=TIMES, blank = True)
	thursday_start = models.CharField(max_length=200, choices=TIMES, blank = True)
	thursday_end = models.CharField(max_length=200, choices=TIMES, blank = True)
	friday_start = models.CharField(max_length=200, choices=TIMES, blank = True)
	friday_end = models.CharField(max_length=200, choices=TIMES, blank = True)
	saturday_start = models.CharField(max_length=200, choices=TIMES, blank = True)
	saturday_end = models.CharField(max_length=200, choices=TIMES, blank = True)


	def __str__(self):
		return self.week
	def get_absolute_url(self):
		return reverse('schedule-detail', args=[str(self.id)])	





#class WeeklySchedule(generic.DetailView): //this feature will display one week and a list of employees working each day with their correlating shifts