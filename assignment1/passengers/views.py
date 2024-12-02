from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Passengers
from .serializers import PassengersSerializerModel
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
@api_view(['GET','POST'])
def passengers(request):
    if request.method == 'GET':
        passenger=Passengers.objects.all()
        serializer=PassengersSerializerModel(passenger,many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer=PassengersSerializerModel(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.err,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def passengers_details(request,pk):
    try:
        passenger=Passengers.objects.get(id=pk)
    except Passengers.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer=PassengersSerializerModel(passenger)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer=PassengersSerializerModel(passenger,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.err,status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        passenger.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


