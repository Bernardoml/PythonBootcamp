
class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ").capitalize()
        self.check_answer(user_answer, current_question.answer)

    # TODO: asking the questions
    def ask_question(self):
        return self.next_question()

    # TODO: checking if answer was correct
    def check_answer(self, user_answer, question_answer):
        if user_answer == question_answer:
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {question_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")

    # TODO: checking if we're at the end of the quiz
    def end_of_quiz(self):
        print("That's the end of the game!")
        print(f"Your final score is: {self.score}/{self.question_number}")
