from django.urls import path
from .  import views

urlpatterns = [
    # path('login/', views.MyLoginView.as_view(), name='login'),
    # path('register/', views.MySignupView.as_view(), name='signup'),
    path('', views.index, name='index'),
    path('profile/edit/',views.editProfile, name='edit-profile'),
    
    path('profile/',views.profile, name="profile"),
    path('profile2/',views.profile2, name="profile2"),
    path('resume/',views.resume,name="resume"),
    path('resume/save/',views.saveResume,name="save-resume"),
]