class User:
    current_score = 0
    total_questions = 0
    def __init__(self, score=0, total=0):
        self.current_score += score
        self.total_questions = total