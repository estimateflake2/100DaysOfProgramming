from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    # --- Button Commands ---
    def true_pressed(self):
        response = self.quiz.check_answer("True")
        print("True button clicked")
        self.give_feedback(response)

    def false_pressed(self):
        response = self.quiz.check_answer("False")
        print("False button clicked")
        self.give_feedback(response)

    def __init__(self, quiz_brain: QuizBrain, question="Amazon acquired Twitch in August 2014 for $970 million dollars."):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz It")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # --- Score Label ---
        self.score_label = Label(
            text="Score: 0",
            fg="white",
            bg=THEME_COLOR,
            font=("Arial", 14, "bold")
        )
        self.score_label.grid(row=0, column=1)

        # --- Question Canvas ---
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150, 125,
            width=280,
            text=question,
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # --- True Button ---
        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(
            image=true_image,
            highlightthickness=3,
            command=self.true_pressed
        )
        self.true_button.image = true_image
        self.true_button.grid(row=2, column=0)

        # --- False Button ---
        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(
            image=false_image,
            highlightthickness=3,
            command=self.false_pressed
        )
        self.false_button.image = false_image
        self.false_button.grid(row=2, column=1)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)
        self.canvas.config(bg="white")

    def give_feedback(self, response: bool):
        """Change the background color based on answer correctness."""
        if response:
            self.canvas.config(bg="#A8E6A1")  # greenish hue
            self.score_label.config(text=f"Score: {self.quiz.get_score()}")
            self.window.after(1000, self.get_next_question)
        else:
            self.canvas.config(bg="#E57373")  # reddish hue
            self.window.after(1000, self.reset_canvas)

    def reset_canvas(self):
        """Resets the canvas background color to white."""
        self.canvas.config(bg="white")
