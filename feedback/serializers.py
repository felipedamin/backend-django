from rest_framework import serializers 
from feedback.models import Employee, Feedback
 
class employeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('employeeId',
                  'employeeName',
                  'officeLocation',
                  'employeeTeam',
                  'points',
                  'lastInteraction')

class feedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ('feedbackId',
                  'officeLocation',
                  'teamName',
                  'feedbackText',
                  'feedbackSentimentAnalysis',
                  'feedbackAspectBasedSA',
                  'feedbackRedFlags',
                  'date')