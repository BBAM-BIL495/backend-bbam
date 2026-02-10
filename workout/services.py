from .models import Exercise, ExerciseRule

class ExerciseLibraryService:
    @staticmethod
    def get_all_exercises():
        return Exercise.objects.all()

    @staticmethod
    def get_rules_for_exercise(exercise_id):
        return ExerciseRule.objects.filter(exercise_id=exercise_id).first()