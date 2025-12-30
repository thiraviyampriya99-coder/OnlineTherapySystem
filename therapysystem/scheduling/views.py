from django.shortcuts import render, redirect
from .models import Session

def home(request):
    return render(request, 'scheduling/home.html')

def therapist_availability(request):
    return render(request, 'scheduling/therapist_availability.html')

def book_session(request):
    if request.method == "POST":
        Session.objects.create(
            patient_name=request.POST.get('patient'),
            therapist_name=request.POST.get('therapist'),
            date=request.POST.get('date'),
            time=request.POST.get('time')
        )
        return redirect('my_sessions')

    return render(request, 'scheduling/book_session.html')

def my_sessions(request):
    sessions = Session.objects.all()
    return render(request, 'scheduling/my_sessions.html', {
        'sessions': sessions
    })

def video_call(request):
    room = "therapy-room-101"
    return redirect(f"https://meet.jit.si/{room}")
