class QuizBrain:
    def __init__(self, list_of_questions):
        self.question_number = 0
        self.list_of_questions = list_of_questions
        self.score = 0

    def next_question(self):
        current_question = self.list_of_questions[self.question_number]
        user_input = input(f"Q{self.question_number + 1}.{current_question.text} (True/False)")
        self.question_number += 1
        self.check_answer(user_input, current_question.answer)

    def still_has_questions(self):
        return self.question_number < len(self.list_of_questions)

    def check_answer(self, user_input, actual_answer):
        if user_input.lower() == actual_answer.lower():
            print('Right')
            self.score += 1
        else:
            print('Wrong')
        print(f'score:{self.score}/{self.question_number}')