from django.db import models
from autoslug import AutoSlugField

class ExamIndex(models.Model):
    exam_name = models.CharField(max_length=200)
    
    university = models.CharField(max_length=100)
    exam_date=models.DateField()
    slug=models.SlugField(blank=True, unique=True)
    
    def __str__(self):
        return self.exam_name
    
    class Meta:
        db_table = "index"
    

class ExamDetails(models.Model):
    exam_index=models.ForeignKey(ExamIndex,on_delete=models.CASCADE)
    exam_description=models.TextField()
    exam_syallabus=models.TextField()
    exam_eligibility=models.TextField()
    exam_official_website=models.URLField()
    courses_offered=models.TextField()
    def __str__(self):
        return self.exam_index.exam_name

# class Exam_resources(models.Model):
#     exam_index=models.ForeignKey(Exam_Index,on_delete=models.CASCADE)
#     exam_resources=models.FileField(upload_to="Exam_Details/Resources")