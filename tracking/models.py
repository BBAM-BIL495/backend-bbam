from django.db import models
from django.contrib.auth.models import User
from workout.models import WorkoutPlans

class WorkoutReminders(models.Model):
    user = models.ForeignKey('users.Users', models.DO_NOTHING)
    plan = models.ForeignKey(WorkoutPlans, models.DO_NOTHING, blank=True, null=True)
    reminder_time = models.TimeField()
    recurrence = models.CharField(max_length=20)
    recurrence_days = models.JSONField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'workout_reminders'


class WorkoutSessions(models.Model):
    user = models.ForeignKey('users.Users', models.DO_NOTHING)
    plan = models.ForeignKey(WorkoutPlans, models.DO_NOTHING, blank=True, null=True)
    plan_name = models.CharField(max_length=255, blank=True, null=True)
    session_date = models.DateField()
    started_at = models.DateTimeField()
    ended_at = models.DateTimeField(blank=True, null=True)
    duration_minutes = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=20)
    overall_accuracy_score = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'workout_sessions'


class SessionExercises(models.Model):
    session = models.ForeignKey('WorkoutSessions', models.DO_NOTHING)
    exercise = models.ForeignKey('workout.Exercises', models.DO_NOTHING)
    step_order = models.IntegerField()
    target_reps = models.IntegerField(blank=True, null=True)
    target_seconds = models.IntegerField(blank=True, null=True)
    completed_reps = models.IntegerField(blank=True, null=True)
    completed_seconds = models.IntegerField(blank=True, null=True)
    accuracy_score = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_exercises'
        unique_together = (('session', 'step_order'),)


class SessionSummaries(models.Model):
    session = models.OneToOneField('WorkoutSessions', models.DO_NOTHING, primary_key=True)
    summary_json = models.JSONField()
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_summaries'