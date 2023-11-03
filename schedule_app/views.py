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
        #context['availability'] = availability  # Add the availability to the context

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

        schedule_instance = ScheduleDetailView()
        schedule_list = schedule_instance.get_queryset()       


        context['schedule_list'] = schedule_list

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
    if request.method == 'POST':
        form = WeekForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('weeks')  # Redirect to a success URL after creating the week
    else:
        form = WeekForm()
    return render(request, 'schedule_app/create_week.html', {'form': form})

def updateWeek(request, pk):
    week_instance = get_object_or_404(Week, pk=pk)
    if request.method == 'POST':
        form = WeekForm(request.POST, instance=week_instance)
        if form.is_valid():
            form.save()
            return redirect('weeks')  # Redirect to a success URL after updating the week
    else:
        form = WeekForm(instance=week_instance)
    return render(request, 'schedule_app/update_week.html', {'form': form})

def deleteWeek(request, pk):
    week_instance = get_object_or_404(Week, pk=pk)
    if request.method == 'POST':
        week_instance.delete()
        return redirect('weeks')  # Redirect to a success URL after deleting the week
    return render(request, 'schedule_app/delete_week.html', {'week': week_instance})

def createSchedule(request, week_id):
    form = ScheduleForm()
    week = Week.objects.get(pk=week_id)
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('week-detail', pk = week_id)  # Redirect to a success URL after creating the week
    else:
        form = ScheduleForm()

    return render(request, 'schedule_app/create_schedule.html', {'form': form})



def updateSchedule(request, schedule_id):
    schedule = get_object_or_404(Schedule, pk=schedule_id)
    week_id = schedule.week.pk
    if request.method == 'POST':
        form = ScheduleForm(request.POST, instance=schedule)
        if form.is_valid():
            form.save()
            return redirect('week-detail', pk = week_id)  # Redirect to a success URL after updating the week
    else:
        form = ScheduleForm(instance=schedule)
    return render(request, 'schedule_app/update_schedule.html', {'form': form})


def deleteSchedule(request, schedule_id):
    schedule = get_object_or_404(Schedule, pk=schedule_id)
    week_id = schedule.week.pk

    if request.method == 'POST':
        schedule.delete()
        # Redirect back to the portfolio detail page
        return redirect('week-detail', pk=week_id)

    context = {'schedule': schedule}
    return render(request, 'schedule_app/delete_schedule.html', context)


#def Calendar(generic.DetailView) Calendar view feature comming soon

def index(request):

# Render the HTML template index.html with the data in the context variable.
   return render( request, 'schedule_app/index.html')

def manager(request):


    return render( request, 'schedule_app/manager_home.html')
