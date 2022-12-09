from django.db import models

Available_CHOICES = (
    ("busy", "busy"),
    ("available", "available"),
)


class WorkDay(models.Model):
    work_day = models.DateField(unique=True)
    def __str__(self):
        return str(self.work_day)

class Employee(models.Model):
    name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    phone_num = models.CharField(max_length=12)
    address = models.CharField(max_length=50)
    curr_status = models.CharField(max_length = 20, choices = Available_CHOICES)
    workday = models.ManyToManyField(WorkDay, default= None, blank= True)

    def work_day(self):
        return ', '.join([str(a.work_day) for a in self.workday.all()])

    def __str__(self):
        return self.name

class MCP(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    capacity = models.FloatField()
    curr_status = models.CharField(max_length = 20, choices = Available_CHOICES)


class Vehicle(models.Model):
    weight = models.FloatField()
    capacity = models.FloatField()
    fuel_capacity = models.FloatField()
    curr_status  = models.CharField(max_length = 20, choices = Available_CHOICES)

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(weight__gt = 0), name='Weight must greater than zero'),
            models.CheckConstraint(check=models.Q(capacity__gt = 0), name='Capacity must greater than zero'),
            models.CheckConstraint(check=models.Q(fuel_capacity__gt = 0), name='Fuel capacity must greater than zero'),
        ]