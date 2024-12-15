from django.shortcuts import render
from .models import Course
from .serializers import CourseSerializer
from rest_framework import status,generics,mixins
from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import viewsets

#assignment 4
class CourseViewSet(viewsets.ModelViewSet):
    queryset=Course.objects.all()
    serializer_class=CourseSerializer
'''
# assignment 3
class CourseList(generics.ListCreateAPIView):
    queryset=Course.objects.all()
    serializer_class=CourseSerializer

class CourseDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset=Course.objects.all()
    serializer_class=CourseSerializer
'''
'''
#assignment 2
class CourseList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset=Course.objects.all()
    serializer_class=CourseSerializer

    def get(self,request):
        return self.list(request)
    
    def post(self,request):
        return self.create(request)
    
class CourseDetails(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset=Course.objects.all()
    serializer_class=CourseSerializer

    def get(self,request,pk):
        return self.retrieve(request,pk)
    
    def put(self,request,pk):
        return self.update(request,pk)

    def delete(self,request,pk):
        return self.destroy(request,pk)
'''
# Create your views here.
'''
#assignment 1
class CourseList(APIView):

    def get(self,request):
        courses=Course.objects.all()
        serializer=CourseSerializer(courses,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)
    
class CourseDetails(APIView):
    def get_object(self,pk):
        try:
            return Course.objects.get(id=pk)
        except Course.DoesNotExist:
            raise Http404
    
    def get(self,request,pk):
        course=self.get_object(pk)
        serializer=CourseSerializer(course)
        return Response(serializer.data)
    
    def put(self,request,pk):
        course=self.get_object(pk)
        serializer=CourseSerializer(course,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        course=self.get_object(pk)
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

'''       


