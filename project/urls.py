from django.urls import path
from .  import views

urlpatterns = [
    path('list/', views.list, name='project-list'),
    path('project-detail/', views.detail, name='project-detail'),

]