from rest_framework import serializers
from .models import WorkoutSessions, SessionExercises, SessionSummaries

class SessionExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = SessionExercises
        fields = ['exercise', 'step_order', 'completed_reps', 'completed_seconds', 'accuracy_score']

class WorkoutSessionSerializer(serializers.ModelSerializer):
    exercises = SessionExerciseSerializer(many=True, read_only=True)

    class Meta:
        model = WorkoutSessions
        fields = ['id', 'plan', 'plan_name', 'session_date', 'started_at', 'ended_at', 
                  'duration_minutes', 'status', 'overall_accuracy_score', 'exercises']

class SessionSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = SessionSummaries
        fields = ['session', 'summary_json']