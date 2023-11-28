from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.views import generic
from django.views.generic import DetailView, ListView
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .decorators import allowed_users
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group
from django.contrib import messages
from .forms import CreateUserForm


# Create your views here.


@method_decorator(login_required(login_url='login'), name='dispatch')
@method_decorator(allowed_users(allowed_roles=['manager_role']), name='dispatch')
class EmployeeListView(generic.ListView):
   model = Employee

@method_decorator(login_required(login_url='login'), name='dispatch')
class EmployeeDetailView(generic.DetailView):
    model = Employee

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)   

        schedule_list_instance = ScheduleListView()
        schedule_list = schedule_list_instance.get_queryset()

        context['schedule_list'] = schedule_list

        return context

@method_decorator(login_required(login_url='login'), name='dispatch')
class ScheduleListView(generic.ListView):
   model = Schedule


@method_decorator(login_required(login_url='login'), name='dispatch')
class ScheduleDetailView(generic.DetailView):
   model = Schedule


@method_decorator(login_required(login_url='login'), name='dispatch')
class AvailabilityDetailView(generic.DetailView):
   model = Availability
   def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)   

        employee_list_instance = EmployeeListView()
        employee_list = employee_list_instance.get_queryset()

        context['employee_list'] = employee_list

        return context

@method_decorator(login_required(login_url='login'), name='dispatch')
class AvailabilityListView(generic.ListView):
   model = Availability

@method_decorator(login_required(login_url='login'), name='dispatch')
class WeekListView(generic.ListView):
    model = Week

@method_decorator(login_required(login_url='login'), name='dispatch')
class WeekDetailView(generic.DetailView):
    model = Week

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        schedule_instance = ScheduleDetailView()
        schedule_list = schedule_instance.get_queryset()       


        context['schedule_list'] = schedule_list

        return context


@login_required(login_url='login')
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



@login_required(login_url='login')
@allowed_users(allowed_roles=['manager_role'])
def createWeek(request):
    if request.method == 'POST':
        form = WeekForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('weeks')  # Redirect to a success URL after creating the week
    else:
        form = WeekForm()
    return render(request, 'schedule_app/create_week.html', {'form': form})

@login_required(login_url='login')
@allowed_users(allowed_roles=['manager_role'])
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


@login_required(login_url='login')
@allowed_users(allowed_roles=['manager_role'])
def deleteWeek(request, pk):
    week_instance = get_object_or_404(Week, pk=pk)
    if request.method == 'POST':
        week_instance.delete()
        return redirect('weeks')  # Redirect to a success URL after deleting the week
    return render(request, 'schedule_app/delete_week.html', {'week': week_instance})

@login_required(login_url='login')
@allowed_users(allowed_roles=['manager_role'])
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


@login_required(login_url='login')
@allowed_users(allowed_roles=['manager_role'])
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
    return render(request, 'schedule_app/update_schedule.html', {'form': form, 'week': schedule.week})



@login_required(login_url='login')
@allowed_users(allowed_roles=['manager_role'])
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

@login_required(login_url='login')
@allowed_users(allowed_roles=['manager_role'])
def manager(request):


    return render( request, 'schedule_app/manager_home.html')

'''@login_required(login_url='login')
@allowed_users(allowed_roles=['manager_role'])
def registerPage(request):

    form = CreateUserForm(request.POST)
    if form.is_valid():
        user = form.save()
        username = form.cleaned_data.get('username')
        group = Group.objects.get(name = 'employee_role')
        user.groups.add(group)
        availability = Availability.objects.create()
        employee = Employee.objects.create(user = user)
        employee.availability = availability
        employee.save()

        messages.success(request, 'Account was created for ' + username)
        return redirect('login')

    context ={'form':form}
    return render(request, 'registration/register.html', context)'''

'''def registerPage(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Handle successful registration, e.g., redirect to login page
            return redirect('employees')
    else:
        form = CreateUserForm()

    return render(request, 'registration/register.html', {'form': form})'''
@login_required(login_url='login')
@allowed_users(allowed_roles=['manager_role'])
def registerPage(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            # Create an Employee instance and link it to the user
            employee, created = Employee.objects.get_or_create(user=user, defaults={'name': form.cleaned_data['employee_name']})
            #print("New Employee created:", employee)
            
            # Print for debugging
            #print("New Employee created:", employee)

            # Create an Availability instance and link it to the employee if it's a new employee
            availability = Availability.objects.create(owner=user.username)

            # Print for debugging
            #print("New Availability created:", availability)

            employee.availability = availability
            employee.save()

            # Assign the user to the 'employee_role' group
            group = Group.objects.get(name='employee_role')
            user.groups.add(group)

            # Save the user now that the employee is linked
            user.save()

            # Redirect to the desired page after successful registration
            return redirect('employees')
    else:
        form = CreateUserForm()

    return render(request, 'registration/register.html', {'form': form})

@login_required(login_url='login')
def userPage(request):
    employee = request.user.employee
    form = EmployeeForm(instance = employee)
    print('employee', employee)
    availability = employee.availability
    print(availability)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES, instance=employee)
        if form.is_valid():
            form.save()
    context = {'availability': availability, 'form':form}
    return render(request,'schedule_app/user.html', context)


'''def prototype(request):

# Render the HTML template index.html with the data in the context variable.
   return render( request, 'schedule_app/schedule_proto.html')'''

@login_required(login_url='login')
@allowed_users(allowed_roles=['manager_role'])
def updateEmployee(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)

    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            # Redirect back to the employee detail page
            return redirect('employees')
    else:
        form = EmployeeForm(instance=employee)  # Pass the instance to pre-fill the form

    context = {'form': form, 'employee': employee}
    return render(request, 'schedule_app/update_employee.html', context)

'''@login_required(login_url='login')
@allowed_users(allowed_roles=['manager_role'])
def deleteWeek(request, pk):
    week_instance = get_object_or_404(Week, pk=pk)
    if request.method == 'POST':
        week_instance.delete()
        return redirect('weeks')  # Redirect to a success URL after deleting the week
    return render(request, 'schedule_app/delete_week.html', {'week': week_instance})'''