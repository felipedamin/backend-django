from rest_framework import serializers 
from feedback.models import Employee
 
class employeeSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Employee
        fields = ('employeeId',
                  'employeeName',
                  'officeLocation',
                  'points',
                  'lastInteraction')
