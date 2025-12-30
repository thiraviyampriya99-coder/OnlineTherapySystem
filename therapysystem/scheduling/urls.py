from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('availability/', views.therapist_availability, name='availability'),
    path('book/', views.book_session, name='book_session'),
    path('my-sessions/', views.my_sessions, name='my_sessions'),
    path('video-call/', views.video_call, name='video_call'),
    ]