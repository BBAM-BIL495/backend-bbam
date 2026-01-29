from django.contrib import admin
from .models import WorkoutSessions, SessionExercises, SessionSummaries

admin.site.register(WorkoutSessions)
admin.site.register(SessionExercises)
admin.site.register(SessionSummaries)