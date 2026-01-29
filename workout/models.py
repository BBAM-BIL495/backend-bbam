from django.db import models
from django.contrib.auth.models import User

class ExerciseRules(models.Model):
    exercise = models.OneToOneField('Exercises', models.DO_NOTHING)
    rules_json = models.JSONField()
    is_active = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'exercise_rules'

class Exercises(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    gif_url = models.CharField(max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'exercises'

class WorkoutPlanItems(models.Model):
    plan = models.ForeignKey('WorkoutPlans', models.DO_NOTHING)
    step_order = models.IntegerField()
    exercise = models.ForeignKey('workout.Exercises', models.DO_NOTHING)
    target_reps = models.IntegerField(blank=True, null=True)
    target_seconds = models.IntegerField(blank=True, null=True)
    set_label = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'workout_plan_items'
        unique_together = (('plan', 'step_order'),)


class WorkoutPlans(models.Model):
    user = models.ForeignKey('users.Users', models.DO_NOTHING)
    plan_name = models.CharField(max_length=255)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'workout_plans'