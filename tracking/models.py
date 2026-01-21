from django.db import models
from django.contrib.auth.models import User
from workout.models import WorkoutPlan, Exercise

class WorkoutSession(models.Model):
    STATUS_CHOICES = [
        ('planned', 'Planned'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plan = models.ForeignKey(WorkoutPlan, on_delete=models.SET_NULL, null=True)
    plan_name = models.CharField(max_length=255, null=True)
    session_date = models.DateField()
    started_at = models.DateTimeField()
    ended_at = models.DateTimeField(null=True, blank=True)
    duration_minutes = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='planned')
    overall_accuracy_score = models.DecimalField(max_digits=5, decimal_places=2, null=True)

    def save(self, *args, **kwargs):
        if self.started_at and self.ended_at:
            delta = self.ended_at - self.started_at
            self.duration_minutes = int(delta.total_seconds() / 60)
        super().save(*args, **kwargs)

class SessionExercise(models.Model):
    session = models.ForeignKey(WorkoutSession, related_name='exercises', on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.RESTRICT)
    step_order = models.IntegerField()
    completed_reps = models.IntegerField(null=True)
    completed_seconds = models.IntegerField(null=True)
    accuracy_score = models.DecimalField(max_digits=5, decimal_places=2, null=True)

class SessionSummary(models.Model):
    session = models.OneToOneField(WorkoutSession, on_delete=models.CASCADE, primary_key=True)
    summary_json = models.JSONField()