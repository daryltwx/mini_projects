from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip
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

    if len(website) <= 0 or len(password) <= 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty! ")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \n\nWebsite: {website}\nEmail: {email} "
                                                    f"\nPassword: {password} \n\n Is it ok to save?")
        if is_ok:
            # Update txt file.
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password} \n")

            # Clear Entries.
            website_entry.delete(0, END)
            password_entry.delete(0, END)


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
website_entry = Entry(width=38)
website_entry.grid(column=1, row=1, columnspan=2)
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




window.mainloop()