from tkinter import *

def button_clicked():
    new_entry = input.get()
    my_label.config(text=new_entry)


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

# Label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

"""
# You can update the text label in both ways as shown below.
my_label["text"] = "New Text"
my_label.config(text="New Text")
"""

# Button
button = Button(text="Click me", command=button_clicked)
button.grid(column=3, row=1)
#button.pack()

# New Button
new_button = Button(text="New Button", command=button_clicked)
new_button.grid(column=1, row=2)


# Entry
input = Entry(width=10)
title = input.get()
input.grid(column=5, row=6)
#input.pack()



window.mainloop()