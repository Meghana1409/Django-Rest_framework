from rest_framework import serializers
from .models import Passengers
class PassengersSerializerModel(serializers.ModelSerializer):
    class Meta:
        model=Passengers
        fields=['id','first_name','last_name','travel_score']
