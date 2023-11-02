from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.views import generic
from django.views.generic import DetailView, ListView
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from .forms import *
from .models import *
# Create your views here.



class EmployeeListView(generic.ListView):
   model = Employee


class EmployeeDetailView(generic.DetailView):
    model = Employee

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        availability_instance = AvailabilityListView()
        availability = availability_instance.get_queryset()       

        schedule_list_instance = ScheduleListView()
        schedule_list = schedule_list_instance.get_queryset()

        context['schedule_list'] = schedule_list
        context['availability'] = availability  # Add the availability to the context

        return context


class ScheduleListView(generic.ListView):
   model = Schedule

class ScheduleDetailView(generic.DetailView):
   model = Schedule

class AvailabilityDetailView(generic.DetailView):
   model = Availability

class AvailabilityListView(generic.ListView):
   model = Availability



def updateAvailability(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    availability, created = Availability.objects.get_or_create(employee=employee)

    if request.method == 'POST':
        form = AvailabilityForm(request.POST, instance=availability)
        if form.is_valid():
            form.save()
            # Redirect back to the employee detail page
            return redirect('employee-detail', employee_id)
    else:
        form = AvailabilityForm(instance=availability)  # Pass the instance to pre-fill the form

    context = {'form': form, 'employee': employee, 'availability': availability}
    return render(request, 'schedule_app/update_availability.html', context)


def createAvailability(request, employee_id):
    form = AvailabilityForm()
    employee = Employee.objects.get(pk=employee_id)
    
    if request.method == 'POST':
        # Create a new dictionary with form data and employee_id
        availability_data = request.POST.copy()
        availability_data['employee_id'] = employee_id
        
        form = AvailabilityForm(availability_data)
        if form.is_valid():
            # Save the form without committing to the database
            availability = form.save(commit=False)
            # Set the employee relationship
            availability.employee = employee
            availability.save()

            # Redirect back to the employee detail page
            return redirect('employee-detail', employee_id)

    context = {'form': form}
    return render(request, 'schedule_app/create_availability.html', context)

#def Calendar(generic.DetailView) Calendar view feature comming soon

def index(request):

# Render the HTML template index.html with the data in the context variable.
   return render( request, 'schedule_app/index.html')
