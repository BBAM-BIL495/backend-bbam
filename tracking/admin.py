from django.contrib import admin
from .models import WorkoutSession, SessionExercise, SessionSummary

class SessionExerciseInline(admin.TabularInline):
    model = SessionExercise
    extra = 0
    readonly_fields = ('accuracy_score',)

@admin.register(WorkoutSession)
class WorkoutSessionAdmin(admin.ModelAdmin):
    list_display = ('user', 'plan_name', 'session_date', 'status', 'overall_accuracy_score')
    list_filter = ('status', 'session_date')
    inlines = [SessionExerciseInline]

@admin.register(SessionSummary)
class SessionSummaryAdmin(admin.ModelAdmin):
    list_display = ('session', 'created_at')