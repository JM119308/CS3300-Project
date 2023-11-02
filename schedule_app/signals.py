# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Employee, Availability

@receiver(post_save, sender=Employee)
def create_availability(sender, instance, created, **kwargs):
    if created:
        Availability.objects.create(employee=instance)
