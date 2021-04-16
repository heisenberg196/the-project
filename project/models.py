from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import User
from django.dispatch import receiver 
from django.db.models.signals import post_save 

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



class Profile(models.Model):   
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	projects = models.ManyToManyField(Project)

	@receiver(post_save, sender=User) #add this
	def create_user_profile(sender, instance, created, **kwargs):
		if created:
			Profile.objects.create(user=instance)

	@receiver(post_save, sender=User) #add this
	def save_user_profile(sender, instance, **kwargs):
		instance.profile.save()