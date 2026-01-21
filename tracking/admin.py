from django.contrib import admin
from .models import WorkoutSession, SessionExercise, SessionSummary

admin.site.register(WorkoutSession)
admin.site.register(SessionExercise)
admin.site.register(SessionSummary)