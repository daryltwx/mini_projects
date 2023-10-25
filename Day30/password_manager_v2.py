from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    letters_list = [choice(letters) for _ in range(randint(8, 10))]
    symbols_list = [choice(symbols) for _ in range(randint(2, 4))]
    numbers_list = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = letters_list + symbols_list + numbers_list
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }


    if len(website) <= 0 or len(password) <= 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty! ")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            # Clear Entries.
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ------------------------- FIND PASSWORD ----------------------------- #

def find_password():
    website = website_entry.get().title()

    # Open JSON
    try:
        with open("data.json", "r") as data_file:
            # Reading old data
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(message="No Data File Found")

    # Get dict
    else:
        try:
            data[website]
        except KeyError:
            messagebox.showinfo(f"No details for the {website} exists.")
        else:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(message=f"Your information from {website} \n\n"
                                f"Email: {email} \n Password: {password}")
            pyperclip.copy(password)

# Only use exception when you don't have an easy alternative.
# if you can use if-else easily, then use it.


## model answer:
"""
def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(message=f"Your information from {website} \n\n"
                                        f"Email: {email} \n Password: {password}")
            pyperclip.copy(password)
        else:
            messagebox.showinfo(message="No details for the {website} exists.")
"""
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady= 50)

# Create bg and img
canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)


# Labels
website_label = Label(text="Website: ")
website_label.grid(column=0, row=1)
username_label = Label(text="Email/Username: ")
username_label.grid(column=0, row=2)
Password_label = Label(text="Password: ")
Password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=21)
website_entry.grid(column=1, row=1)
website_entry.focus()
email_entry = Entry(width=38)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "name@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, columnspan=1)

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3)
add_button = Button(text="Add", width=35, command=save)
add_button.grid(column=1, row=4, columnspan=2)
search_button = Button(text="Search", width=13, command=find_password)
search_button.grid(column=2, row=1)





window.mainloop()