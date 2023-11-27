from django import forms
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

'''class CreateUserForm(UserCreationForm):

	class Meta:
		model = User
		fields = ['username', 'email', 'password1','password2']'''


class CreateUserForm(UserCreationForm):
    phone = forms.CharField(max_length=20)
    status = forms.ChoiceField(choices=[('Full-Time', 'Full-time'), ('Part-Time', 'Part-time')])
    employee_name = forms.CharField(max_length=200, required=True)

    class Meta:
        model = User
        fields = ['username','employee_name', 'email', 'phone', 'status', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.save()

        # Create an Employee instance and link it to the user
        employee = Employee.objects.create(user=user, name=self.cleaned_data['employee_name'])
        employee.phone = self.cleaned_data['phone']
        employee.status = self.cleaned_data['status']
        employee.save()

        return user

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
