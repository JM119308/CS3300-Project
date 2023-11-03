from django.forms import ModelForm
from .models import *

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



	#Prefill week into the form
	'''def __init__(self, *args, **kwargs):
		super(ScheduleForm, self).__init__(*args, **kwargs)
		instance = kwargs.get('instance')
		if instance:
			self.fields['week'].disabled = True  # Replace 'your_field_name' with the name of your field'''
