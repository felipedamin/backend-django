import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import F
from django.utils import timezone
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework import status, viewsets
from rest_framework.views import APIView
from feedback.models import Employee, Feedback
from feedback.serializers import employeeSerializer, feedbackSerializer
from feedback.redflag import redflag
from sentimentAnalysis.sentiment_analysis import sentiment_pt as sentimentAnalysis
from aspectBasedSentimentAnalysis.AB_sentiment_analysis import feature_sentiment as aspectBasedSA
from feedback.wordCloud import show_wordcloud

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
            eid = request.query_params.get('id', None)
            order_by = request.query_params.get('order_by', None)
            employees = Employee.objects.all()
            
            if name is not None:
                employees = employees.filter(employeeName__icontains=name)

            if eid is not None:
                employees = employees.filter(employeeId=eid)
                
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
            employeeId = request.data.get('employeeId')
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

class employeeTopScores(APIView):
    def get(self, request, *args, **kwargs):
        # Parse query parameters
        try:
            office = request.query_params.get('office', None)
            employees = Employee.objects.all()
            
            if office is not None:
                employees = employees.filter(officeLocation=office)
    
            # order filtered list
            employees = employees.order_by('-points')
            
            # assuming obj is your model instance
            serializer = employeeSerializer(employees, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            data = {
                "message" : e,
                "code": 2,
            }
            return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class employeeFeedback(APIView):
    def get(self, request):
        try:
            feedbackId = request.query_params.get('feedbackid', None)
            teamName = request.query_params.get('teamname', None)
            teamSupervisor = request.query_params.get('teamsupervisor', None)
            officeLocation = request.query_params.get('officelocation', None)

            feedbacks = Feedback.objects.all()

            if feedbackId is not None:
                feedbacks = feedbacks.filter(feedbackId=feedbackId)
            if teamName is not None:
                feedbacks = feedbacks.filter(teamName__icontains=teamName)
            if teamSupervisor is not None:
                feedbacks = feedbacks.filter(teamSupervisor=teamSupervisor)
            if officeLocation is not None:
                feedbacks = feedbacks.filter(officeLocation=officeLocation)
            
            
            serializer = feedbackSerializer(feedbacks, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            data = {
                "message" : e,
                "code": 2,
            }
            return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request, *args, **kwargs):
        print('postinf feedback')
        try:
            employeeId = request.data.get('employeeId')
            feedbackText = request.data.get('feedbackText'),
            
            if employeeId is not None:
                # increment employee points
                employee = Employee.objects.filter(employeeId=employeeId).update(points=F('points')+3)

            # look for red flags
            print('redflags')
            redflags = redflag(feedbackText[0])
            print(redflags)
            
            # SA
            print('feedbackSA')
            feedbackSA = sentimentAnalysis(feedbackText[0])
            print(feedbackSA)
            
            # AB_SA
            print('feedbackABSA')
            feedbackABSA = aspectBasedSA(feedbackText[0])
            print(feedbackABSA)
                        
            feedback = Feedback.objects.create(
                feedbackText=feedbackText[0],
                teamName=request.data.get('teamName'),
                teamSupervisor=request.data.get('teamSupervisor'),
                officeLocation=request.data.get('officeLocation'),
                feedbackSentimentAnalysis=str(feedbackSA),
                feedbackAspectBasedSA=str(feedbackABSA),
                feedbackRedFlags=str(redflags),
                )
            
            return Response("feedback received", status=status.HTTP_200_OK)
        except Exception as e:
            data = {
                "message" : e,
                "code": 2,
            }
            return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class WordCloud(APIView):
    def get(self, request):
        feedbacks = Feedback.objects.all()
        
        feedbacks = feedbacks.order_by('-date')
        feedbacks = feedbacks.filter(feedbackRedFlags__exact='')[:50]
        feedbacksString = ''
        for f in feedbacks:
            feedbacksString += f.feedbackText
            feedbacksString += ' '
        print(feedbacksString)
        show_wordcloud(feedbacksString)
        return Response("wordcloud generated", status=status.HTTP_200_OK)


class RedFlags(APIView):
    def get(self, request):
        feedbacks = Feedback.objects.all()
        feedbacks = feedbacks.order_by('-date')
        feedbacks = feedbacks.exclude(feedbackRedFlags__exact='')

        serializer = feedbackSerializer(feedbacks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)