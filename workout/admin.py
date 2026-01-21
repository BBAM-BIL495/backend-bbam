from django.contrib import admin
from .models import Exercise, ExerciseRule, WorkoutPlan, WorkoutPlanItem

admin.site.register(Exercise)
admin.site.register(ExerciseRule)
admin.site.register(WorkoutPlan)
admin.site.register(WorkoutPlanItem)