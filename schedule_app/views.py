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

class WeekListView(generic.ListView):
    model = Week

class WeekDetailView(generic.DetailView):
    model = Week

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        week_instance = WeekListView()
        week = week_instance.get_queryset()       


        context['week_list'] = week_list

        return context

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


def createWeek(request):
    form = WeekForm()
    
    if request.method == 'POST':
        
        if form.is_valid():
            # Save the form without committing to the database
            week = form.save(commit=False)
            week.save()

            # Redirect back to the weeks page
            return redirect('weeks')

    context = {'form': form}
    return render(request, 'schedule_app/create_week.html', context)

#def Calendar(generic.DetailView) Calendar view feature comming soon

def index(request):

# Render the HTML template index.html with the data in the context variable.
   return render( request, 'schedule_app/index.html')

def manager(request):

# Render the HTML template index.html with the data in the context variable.
   return render( request, 'schedule_app/manager_home.html')