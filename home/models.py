from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver 
from django.db.models.signals import post_save
from project.models import Project
from django.utils import timezone


# Create your models here.
# class Profile(models.Model):   
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     # projects = models.ManyToManyField(Project, blank=None, null=True)
#     name = models.CharField(verbose_name="Email" max_length=90)
#     email = models.EmailField(verbose_name="Email", )

# 	@receiver(post_save, sender=User) #add this
# 	def create_user_profile(sender, instance, created, **kwargs):
# 		if created:
# 			Profile.objects.create(user=instance)

# 	@receiver(post_save, sender=User) #add this
# 	def save_user_profile(sender, instance, **kwargs):
# 		instance.profile.save()

class Skill(models.Model):
    Skill_Rating = (
        ('B', 'Beginner'),
        ('I', 'Intermediate'),
        ('A', 'Advance'),
    )
    name = models.CharField(verbose_name="Skill Name", max_length=20)
    rating = models.CharField(verbose_name="Skill Rating", max_length=1, choices=Skill_Rating)
    # user = models.ForeignKey(
    #     User, related_name='skills', on_delete=models.CASCADE, default=0)
    def __str__(self) -> str:
        return f'{self.name} - {self.rating}'

# class Experience(models.Model):
#     designation = models.CharField(verbose_name='Job Profile', max_length=50)
#     organization = models.CharField(verbose_name='Organization', max_length=50)
#     location = models.CharField(verbose_name='Location', max_length=50, default='work from home', blank=True, null=True)
#     start_date = models.DateField( blank=True, null=True)
#     end_date = models.DateField( blank=True, null=True)
#     description = models.TextField( blank=True, null=True)
#     def __str__(self) -> str:
#         return f'{self.designation} - {self.organization}'

class SavedProjects(models.Model):
    project = models.ForeignKey(
        Project, related_name='saved_project', on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, related_name='saved', on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.job.title


class AppliedJobs(models.Model):
    job = models.ForeignKey(
        Project, related_name='applied_project', on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, related_name='applied_project', on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.job.title
        
def def_skill():
    return Skill.objects.create(name='Team Work', rating='I')

class Profile(models.Model):
    # GENDER_CHOICES = (
    #     ('M', 'Male'),
    #     ('F', 'Female'),
    # )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='team-3.jpg', upload_to='profile_pics')
    # gender_choice = models.CharField(verbose_name="Gender", max_length=1, choices=GENDER_CHOICES)
    phone = models.CharField(max_length=14, blank=True, null=True)
    country = models.CharField(max_length=35, blank=True, null=True)
    city = models.CharField(max_length=35, blank=True, null=True)
    skills = models.ManyToManyField(Skill, blank=True, null=True, default=def_skill, editable=True)
    # experience = models.ManyToManyField(Experience, blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def get_absolute_url(self):
	    return "/users/{}".format(self.slug)


User.profile = property(lambda u: Profile.objects.get_or_create(user=u)[0])
