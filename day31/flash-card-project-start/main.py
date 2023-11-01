from tkinter import *
import pandas as pd
import random


BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}
# ------------------ Data --------------
try:
    df = pd.read_csv("/Users/Pandaphy/github/mini_projects/day31/flash-card-project-start/data/words_to_learn.csv")

except FileNotFoundError:
    original_data = pd.read_csv("/Users/Pandaphy/github/mini_projects/day31/flash-card-project-start/data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = df.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_bg, image=front_img)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_bg, image=back_img)

def is_known():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

# ---- UI ----
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
front_img = PhotoImage(file="/Users/Pandaphy/github/mini_projects/day31/flash-card-project-start/images/card_front.png")
back_img = PhotoImage(file="/Users/Pandaphy/github/mini_projects/day31/flash-card-project-start/images/card_back.png")
card_bg = canvas.create_image(400, 263, image=front_img)
card_title = canvas.create_text(400, 150, fill="Black", text="title", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, fill="Black", text="word", font=("Arial", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# import img

right_img = PhotoImage(file="/Users/Pandaphy/github/mini_projects/day31/flash-card-project-start/images/right.png")
wrong_img = PhotoImage(file="/Users/Pandaphy/github/mini_projects/day31/flash-card-project-start/images/wrong.png")

# Buttons
right_button = Button(image=right_img, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, borderwidth=0, command=is_known)
right_button.grid(row=1, column=1)
wrong_button = Button(image=wrong_img, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, borderwidth=0, command=next_card)
wrong_button.grid(row=1, column=0)


next_card()


window.mainloop()




