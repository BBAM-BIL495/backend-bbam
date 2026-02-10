class AIFeedbackEngine:
    @staticmethod
    def process_error_vector(error_vector):
        if error_vector.get('something_angle') > 90:
            return "error generating test"
        return "form looks great............."
    
    @staticmethod
    def generate_feedback(error_vector):
        if error_vector.get('something_angle') > 90:
            return "error generating test"
        return "form looks great............."

class PerformanceDataProcessor:
    @staticmethod
    def process_incoming_session(data):
        return data

class PerformanceAnalyzer:
    @staticmethod
    def calculate_overall_score(session):
        exercises = session.sessionexercise_set.all()
        if not exercises: return 0
        return sum(e.accuracy_score for e in exercises) / len(exercises)
    
    @staticmethod
    def generate_and_save_summary(session):
        exercises = session.sessionexercise_set.all()
        
        summary_data = {
            "overall_avg_score": float(session.overall_accuracy_score),
            "total_completed_reps": sum(e.completed_reps or 0 for e in exercises),
            "details": [
                {"name": e.exercise.name, "score": float(e.accuracy_score)} for e in exercises
            ]
        }
        
        SessionSummary.objects.update_or_create(
            session=session,
            defaults={"summary_json": summary_data}
        )

class ProgressAnalyzer:
    @staticmethod
    def get_user_trends(user_id): pass