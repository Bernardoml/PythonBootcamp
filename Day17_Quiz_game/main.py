from quiz_brain import QuizBrain
from question_model import Question
from data import question_data

question_bank = []

for item in question_data:
    new_q = Question(item['text'], item['answer'])
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    answer = quiz.ask_question()

quiz.end_of_quiz()
