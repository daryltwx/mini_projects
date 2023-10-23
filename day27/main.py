from tkinter import *

def button_clicked():
    miles_entry = int(input.get())
    to_km = round(miles_entry*1.60934)
    convert_km_label.config(text=to_km)


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=100, height=50)
window.config(padx=10, pady=10)

# Miles - Label
miles_label = Label(text="Miles")
miles_label.grid(column=3, row=0)

# Miles - Entry
input = Entry(width=5)
input.insert(END, string="0")
miles_input = input.get()
input.grid(column=2, row=0)

# "is equal to" - Label
is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=1, row=1)

# Km - Label
km_label = Label(text="Km")
km_label.grid(column=3, row=1)

# Km convert - Label
convert_km_label = Label(text="0")
convert_km_label.grid(column=2, row=1)

# Calculate - Button
cal_button = Button(text="Calculate", command=button_clicked)
cal_button.grid(column=2, row=2)
"""
# You can update the text label in both ways as shown below.
my_label["text"] = "New Text"
my_label.config(text="New Text")
"""





#input.pack()



window.mainloop()