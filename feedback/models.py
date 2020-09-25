from django.db import models

# Create your models here.

class Employee(models.Model):
    #Fields
    employeeId = models.AutoField(primary_key=True)
    employeeName = models.CharField(max_length=100)
    employeeTeam = models.CharField(max_length=100)
    officeLocation = models.CharField(max_length=100)
    points = models.IntegerField()
    lastInteraction = models.DateTimeField(auto_now=True)
 
    #Metadata
    class Meta:
        ordering = ['employeeId']
 
    #Methods
    def __str__(self):
        return str(self.employeeName + ' id: ' + str(self.employeeId))

class Team(models.Model):
    #Fields
    teamId = models.AutoField(primary_key=True)
    teamName = models.CharField(max_length=100)
    teamSupervisor = models.ForeignKey('Employee', on_delete=models.PROTECT)
    officeLocation = models.CharField(max_length=100)
    
    #Metadata
    class Meta:
        ordering = ['teamSupervisor']
 
    #Methods
    def __str__(self):
        return str(self.teamName)

class Feedback(models.Model):
    #Fields
    feedbackId = models.AutoField(primary_key=True)
    teamName = models.CharField(max_length=100)
    teamSupervisor = models.ForeignKey('Employee', on_delete=models.PROTECT, blank=True, null=True)
    officeLocation = models.CharField(max_length=100)
    feedbackText = models.CharField(max_length=1000)
    feedbackSentimentAnalysis = models.CharField(max_length=1000, blank=True)
    feedbackAspectBasedSA = models.CharField(max_length=1000, blank=True)
    feedbackRedFlags = models.CharField(max_length=1000, blank=True)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    
    #Methods
    def __str__(self):
        return str(self.feedbackText[0:20])
