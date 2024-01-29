from django.db import models

class Exam_Details(models.Model):
    name = models.CharField(max_length=200)
    university = models.CharField(max_length=100)
    exam_date=models.DateField()
    
    class Meta:
        db_table = "index"


