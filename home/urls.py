from django.urls import path
from .  import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.signup, name='signup'),
    path('', views.index, name='index'),
    path('profile/',views.profile, name="profile"),
    path('profile2/',views.profile2, name="profile2"),
]