from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Project(models.Model):
    project_name = models.CharField(max_length=90, verbose_name='Project Name')
    # project_cateogory = 
    
    image = models.FileField(upload_to='images/', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    tech_used = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
def __str__(self):
    return "{title} by {creator}".format(title=self.project_name, creator=self.creator.first_name) 



