from django.db import models
from django.contrib.auth.models import User

class Exercise(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    gif_url = models.URLField(max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class ExerciseRule(models.Model):
    exercise = models.OneToOneField(Exercise, on_delete=models.CASCADE, related_name='rules')
    rules_json = models.JSONField()
    is_active = models.BooleanField(default=True)

class WorkoutPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plan_name = models.CharField(max_length=255)
    deleted_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class WorkoutPlanItem(models.Model):
    plan = models.ForeignKey(WorkoutPlan, related_name='items', on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.RESTRICT)
    step_order = models.IntegerField()
    target_reps = models.IntegerField(null=True, blank=True)
    target_seconds = models.IntegerField(null=True, blank=True)
    set_label = models.IntegerField(null=True, blank=True)

    class Meta:
        unique_together = ('plan', 'step_order')