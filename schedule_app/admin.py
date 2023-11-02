from django.contrib import admin
from .models import *

# Register your models here so they can be edited in admin panel
admin.site.register(Employee)
admin.site.register(Schedule)
admin.site.register(Availability)
admin.site.register(Week)