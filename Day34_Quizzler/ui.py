import tkinter
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = tkinter.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = tkinter.Label(
            text=f"Score: {self.quiz.score}",
            bg=THEME_COLOR,
            fg="white",
            font=("Arial", 20, "italic"))
        self.score_label.grid(column=1, row=0)

        self.canvas = tkinter.Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text=f"test",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        false_img = tkinter.PhotoImage(file="images/false.png")
        self.false_button = tkinter.Button(image=false_img, highlightthickness=0, command=self.answer_false)
        self.false_button.grid(column=0, row=2)

        true_img = tkinter.PhotoImage(file="images/true.png")
        self.true_button = tkinter.Button(image=true_img, highlightthickness=0, command=self.answer_true)
        self.true_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def answer_true(self):
        # passing the first function return as a param (1 step)
        self.give_feedback(self.quiz.check_answer("True"))

    def answer_false(self):
        # passing the variable is_right as param (2 steps)
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
