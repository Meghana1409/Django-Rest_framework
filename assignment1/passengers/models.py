from django.db import models

# Create your models here.
class Passengers(models.Model):
    id=models.AutoField(primary_key=True)
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    travel_score=models.IntegerField()

    class __meta__():
        table_name='passengers'
        

