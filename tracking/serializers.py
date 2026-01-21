from rest_framework import serializers
from .models import WorkoutSession, SessionExercise, SessionSummary

class SessionExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = SessionExercise
        fields = ['exercise', 'step_order', 'completed_reps', 'completed_seconds', 'accuracy_score']

class WorkoutSessionSerializer(serializers.ModelSerializer):
    exercises = SessionExerciseSerializer(many=True, read_only=True)

    class Meta:
        model = WorkoutSession
        fields = ['id', 'plan', 'plan_name', 'session_date', 'started_at', 'ended_at', 
                  'duration_minutes', 'status', 'overall_accuracy_score', 'exercises']

class SessionSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = SessionSummary
        fields = ['session', 'summary_json']