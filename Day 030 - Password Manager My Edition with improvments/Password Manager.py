from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
import pyperclip
import json


# ---------------------------- SEARCH FUNCTION ------------------------------- #

def find_password():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Here is your info:\n\n"
                                                       f"Email:   {email}\nPassword:   {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No Details For '{website}' Exists")


# ---------------------------- COMPLEX PASSWORD GENERATOR  ------------------------------- #


def generate_password_complex():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- EASY PASSWORD GENERATOR ------------------------------- #

def generate_password_easy():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
               'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
               'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    password_letters = [choice(letters) for _ in range(randint(8, 10))]

    password_list = password_letters
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

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don`t leave any fields empty!")
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
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)

canvas = Canvas(width=200, height=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:", )
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:", )
email_label.grid(column=0, row=2)
password_label = Label(text="Password:", )
password_label.grid(column=0, row=3, rowspan=2)


# Entries
website_entry = Entry(width=37)
website_entry.grid(column=1, row=1)
website_entry.focus()
email_entry = Entry(width=37)
email_entry.grid(column=1, row=2)
password_entry = Entry(width=37, )
password_entry.grid(column=1, row=3, rowspan=2)

# Buttons
search_button = Button(text="Search", width=10, command=find_password)
search_button.grid(column=2, row=1)
generate_complex_button = Button(text="Complex", command=generate_password_complex)
generate_complex_button.grid(column=2, row=3, sticky="nsew")
generate_easy_button = Button(text="Easy", command=generate_password_easy)
generate_easy_button.grid(column=2, row=4, sticky="nsew")
add_button = Button(text="Add", width=45, command=save)
add_button.grid(column=1, row=5, columnspan=2)


window.mainloop()
