from django.db import models
class Patient(models.Model):
      id=models.IntegerField(primary_key=True)
      name=models.CharField(max_length=100)
      age=models.IntegerField()
      gender=models.CharField(max_length=10)
      disease=models.CharField(max_length=200)
      admitted_date=models.DateField()

def __str__(self):
    return self.name