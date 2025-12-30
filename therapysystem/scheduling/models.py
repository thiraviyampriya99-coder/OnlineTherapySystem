from django.db import models
from django.conf import settings

class TherapistAvailability(models.Model):
    therapist = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f'{self.therapist.username} - {self.date}'


class Session(models.Model):

    STATUS_CHOICES = [
        ('booked', 'Booked'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    patient = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='patient_sessions'
    )
    therapist = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='therapist_sessions'
    )

    date = models.DateField()
    time = models.TimeField()

    room_name = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='booked')
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.patient.username} -> {self.therapist.username} ({self.status})'
