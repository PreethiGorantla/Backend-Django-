from django.db import models
from django.contrib.auth.models import User
class Patient(models.Model):
      #id=models.IntegerField(primary_key=True)
      user = models.ForeignKey(User, on_delete=models.CASCADE)
      age=models.IntegerField()
      gender=models.CharField(max_length=10)
      disease=models.CharField(max_length=200)
      admitted_date=models.DateField()

      def __str__(self):
          return self.user.username