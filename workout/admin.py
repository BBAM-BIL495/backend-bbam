from django.contrib import admin
from .models import Exercises, ExerciseRules, WorkoutPlans, WorkoutPlanItems

admin.site.register(Exercises)
admin.site.register(ExerciseRules)
admin.site.register(WorkoutPlans)
admin.site.register(WorkoutPlanItems)