from django.db import models

# Create your models here.
class Course(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length= 100)
    description=models.CharField(max_length=500)
    rating=models.DecimalField(max_digits=10,decimal_places=3)

    def __str__(self):
        return self.id+self.name

