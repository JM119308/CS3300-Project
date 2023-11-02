from django.forms import ModelForm
from .models import *

class AvailabilityForm(ModelForm):
	class Meta:
		model = Availability
		fields = ('sunday_start', 'sunday_end', 'monday_start', 'monday_end','tuesday_start', 'tuesday_end', 
			'wednesday_start', 'wednesday_end', 'thursday_start', 'thursday_end', 
			'friday_start', 'friday_end', 'saturday_start', 'saturday_end')
