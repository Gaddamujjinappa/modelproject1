from django.db import models

# Create your models here.
class job(models.Model):
    jobname=models.CharField(max_length=64)
    jobid=models.IntegerField()
    jobsal=models.FloatField()
    jobage=models.IntegerField()
    
    def __str__(self):
        return self.jobname
