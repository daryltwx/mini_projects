from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.canvas()
        self.text_boxes(score=0)
        self.buttons()

        self.window.mainloop()

    def buttons(self):
        self.true_img = PhotoImage(file="/Users/Pandaphy/github/mini_projects/day34/quizzler-app-start/images/true.png")
        self.false_img = PhotoImage(file="/Users/Pandaphy/github/mini_projects/day34/quizzler-app-start/images/false.png")
        self.true_button = Button(image=self.true_img, highlightthickness=0)
        self.true_button.grid(row=1, column=0)
        self.false_button = Button(image=self.false_img, highlightthickness=0)
        self.false_button.grid(row=1, column=1)


    def canvas(self):
        self.canvas = Canvas(width=400, height=500)
        self.canvas.create_rectangle(50, 50, 350, 350, fill="white", width=2)
        self.canvas.grid(row=0, column=0, columnspan=2)

    def text_boxes(self, score):
        question_title = self.canvas.create_text(200, 163, fill="Black", text="questions", font=("Arial", 20))
        score_title = self.canvas.create_text(300, 23, fill="white", text=f"Score: {score}", font=("Arial", 10))