from django.db import models

# Create your models here.

class Employee(models.Model):
    '''A class representing a model derived from Model class'''
    
    #Fields
    employeeId = models.CharField(primary_key=True, max_length=1000)
    employeeName = models.CharField(max_length=1000)
    officeLocation = models.CharField(max_length=1000)
    points = models.IntegerField()
    lastInteraction = models.DateTimeField()
 
    #Metadata
    class Meta:
        ordering = ['points']
 
    #Methods
    def __str__(self):
        return str(self.employeeId + 'has: ' + self.points + ' points.')

class Team(models.Model):
    '''A class representing a model derived from Model class'''
    
    #Fields
    teamName = models.CharField(max_length=1000)
    teamSupervisor = models.ForeignKey('Employee', on_delete=models.PROTECT)
    officeLocation = models.CharField(max_length=1000)
    
    #Metadata
    class Meta:
        ordering = ['teamSupervisor']
 
    #Methods
    def __str__(self):
        return str(self.teamName)