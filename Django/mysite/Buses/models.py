from django.db import models

# Create your models here.

class Bus_Model(models.Model):
    bus_number = models.CharField(max_length=100,null=False)
    bus_type = models.CharField(max_length=100,null=False)
    driver_name = models.CharField(max_length=200)
    driver_contact = models.CharField(max_length=50)
    capacity = models.CharField(max_length=50,null=False)
    origin_location = models.CharField(max_length=200)
    end_location = models.CharField(max_length=200)
    last_maintenance = models.DateField()
    next_maintenance = models.DateField()
    status = models.CharField(null=False,max_length=50) #Running, Under Maintenance , idle
    start_time = models.TimeField() #starting of bus Schedule
    end_time = models.TimeField() #End time of bus Schedule time
    on_time = models.BooleanField(null=True) #suggest if the bus is following the time schedule it should be at
