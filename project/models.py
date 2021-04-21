from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Project(models.Model):
    # Project_Category = (
    #     ('webdev', 'Web Development'),
    #     ('anddev', 'Android Development'),
    #     ('ml', 'Machine Learning'),
    #     ('gd', 'Graphic'),
    # )
    project_name = models.CharField(max_length=90, verbose_name='Project Name')
    # rating = models.CharField(verbose_name="Skill Rating", max_length=1, choices=Skill_Rating)
    description = models.CharField(max_length=320, verbose_name='Project Description')
    
    image = models.FileField(upload_to='images/', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    tech_used = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
            return f'{self.project_name} by {self.creator}'




