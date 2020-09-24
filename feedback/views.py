from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework import status, viewsets
from rest_framework.views import APIView
from feedback.models import Employee
from feedback.serializers import employeeSerializer
from django.utils import timezone
import datetime

# Create your views here.
def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

class employeeView(APIView):
    def get(self, request, *args, **kwargs):
        # Parse query parameters
        try:
            name = request.query_params.get('name', None)
            order_by = request.query_params.get('order_by', None)
            employees = Employee.objects.all()
            if name is not None:
                employees = employees.filter(employeeName__icontains=name)
                
            # order filtered list
            if order_by is not None:
                employees = employees.order_by(order_by)
            
            # assuming obj is your model instance
            serializer = employeeSerializer(employees, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            data = {
                "message" : e,
                "code": 2,
            }
            return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def post(self, request, *args, **kwargs):
        try:
            employeeId = request.data.get('id')
            aux = {
                "employeeName": request.data.get('name'),
                "officeLocation": request.data.get('office'),
                "points": request.data.get('points'),
                "lastInteraction": datetime.datetime.now(tz=timezone.utc)
            }
            employee, created = Employee.objects.get_or_create(employeeId=employeeId,  defaults=aux)

            if created:
                return Response("employee created", status=status.HTTP_201_CREATED)
            
            return Response("employee already exists", status=status.HTTP_200_OK)
        except Exception as e:
            data = {
                "message" : e,
                "code": 2,
            }
            return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)