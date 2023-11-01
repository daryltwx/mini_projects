from tkinter import *
import pandas as pd
import random


BACKGROUND_COLOR = "#B1DDC6"
# ------------------ Data --------------

df = pd.read_csv("/Users/Pandaphy/github/mini_projects/day31/flash-card-project-start/data/french_words.csv")
to_learn = df.to_dict(orient="records")

# Create a list with randomised 1 - 100
numbers = list(range(len(df)))
random.shuffle(numbers)
print(numbers)

def next_card():
    current_card = random.choice(to_learn)
    language_label.config(text="French")
    word_label.config(text=f"{current_card['French']}")


def flip_card():

# ---- UI ----
window = Tk()
window.title("Flashy")
window.minsize(width=1000, height=700)

window.after(3000, func=flip_card)
canvas = Canvas(width=1000, height=700, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.place(x=0, y=0)






# ---- UI ----

# import img
front_img = PhotoImage(file="/Users/Pandaphy/github/mini_projects/day31/flash-card-project-start/images/card_front.png")
back_img = PhotoImage(file="/Users/Pandaphy/github/mini_projects/day31/flash-card-project-start/images/card_back.png")
right_img = PhotoImage(file="/Users/Pandaphy/github/mini_projects/day31/flash-card-project-start/images/right.png")
wrong_img = PhotoImage(file="/Users/Pandaphy/github/mini_projects/day31/flash-card-project-start/images/wrong.png")

front = canvas.create_image(510, 300, image=front_img)
# back = canvas.create_image(510, 300, image=back_img)

language = "Title"
word = "word"
front_card = "white"
back_card = "black"
card = front_card

# Labels
language_label = Label(text=language, fg="black", bg=card, font=("Ariel", 40, "italic"))
language_label.place(x=450, y=150)
word_label = Label(text=word, fg="black", bg=card, font=("Ariel", 60, "bold"))
word_label.place(x=425, y=263)

# Buttons
right_button = Button(image=right_img, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, borderwidth=0, command=next_card)
right_button.place(x=700, y=570)
wrong_button = Button(image=wrong_img, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, borderwidth=0, command=next_card)
wrong_button.place(x=200, y=570)

next_card()


window.mainloop()






#### ---- Unused codes ----

# french_dict = {row.French: row.English for (French, row) in df.iterrows()}
# print(french_dict)

# random_word = random.randint(0, len(df))
# print(df["French"][random_word], df["English"][random_word])

# Create a list of words in random order
# Make the df in to a dict

