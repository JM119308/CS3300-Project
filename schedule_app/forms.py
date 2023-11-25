from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class AvailabilityForm(ModelForm):
	class Meta:
		model = Availability
		fields = ('sunday_start', 'sunday_end', 'monday_start', 'monday_end','tuesday_start', 'tuesday_end', 
			'wednesday_start', 'wednesday_end', 'thursday_start', 'thursday_end', 
			'friday_start', 'friday_end', 'saturday_start', 'saturday_end')

class WeekForm(ModelForm):
	class Meta:
		model = Week
		fields = ('weekDate',)

class ScheduleForm(ModelForm):
	class Meta:
		model = Schedule
		fields = ('week','employee','sunday_start', 'sunday_end', 'monday_start', 'monday_end','tuesday_start', 'tuesday_end', 
			'wednesday_start', 'wednesday_end', 'thursday_start', 'thursday_end', 
			'friday_start', 'friday_end', 'saturday_start', 'saturday_end')

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1','password2']

class EmployeeForm(ModelForm):
	class Meta:
		model = Employee
		fields = '__all__'
		exclude = ['user', 'availability']

	#Prefill week into the form
	'''def __init__(self, *args, **kwargs):
		super(ScheduleForm, self).__init__(*args, **kwargs)
		instance = kwargs.get('instance')
		if instance:
			self.fields['week'].disabled = True  # Replace 'your_field_name' with the name of your field'''
