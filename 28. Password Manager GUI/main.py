from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

FONT_LABELS = ("Courier", 14, "bold")
FONT_ENTRY = ("Arial", 14, "normal")
FONT_BUTTONS = ("Courier", 10, "bold")
STARTING_EMAIL = "jakub.szpytka@gmail.com"

# ---------------------------- SEARCH DATABASE ------------------------------- #

def find_password():
    check = website_entry.get().capitalize()
    login_key = "email"
    password_key = "password"
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            messagebox.showinfo(title=f"{check}", message=f"Login: {data[check][login_key]}\n"
                                                          f"Password: {data[check][password_key]}")
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    except KeyError:
        messagebox.showinfo(title="Oops", message="No details for the website exists")

# ---------------------------- RESET EMAIL ENTRY ------------------------------- #

def reset_email():
    login_entry.delete(0, END)
    login_entry.insert(0, STARTING_EMAIL)

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
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
    new_password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, new_password)
    pyperclip.copy(new_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_to_file():
    website_text = website_entry.get().capitalize()
    login_text = login_entry.get()
    password_text = password_entry.get()
    if len(website_text) == 0 or len(login_text) == 0 or len(password_text) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website_text,
                                       message=f"These are the details entered:\n"
                                               f"Login: {login_text}\nPassword: {password_text}\n"
                                               f"Is it ok to save?")
        if is_ok:
            new_data = {
                website_text: {
                    "email": login_text,
                    "password": password_text,
                }
                        }
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)
                website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #
# WINDOW
window = Tk()
window.config(padx=20, pady=20)
window.title("Password Manager")

# CANVAS
logo_img = PhotoImage(file="logo.png")
canvas = Canvas(height=200, width=200, highlightthickness=0)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# LABELS
website = Label(text="Website:", font=FONT_LABELS)
website.grid(column=0, row=1)
login = Label(text="Email/Username:", font=FONT_LABELS)
login.grid(column=0, row=2)
password = Label(text="Password:", font=FONT_LABELS)
password.grid(column=0, row=3)

# INPUTS
website_entry = Entry(width=21, font=FONT_ENTRY)
website_entry.grid(column=1, row=1)
website_entry.focus()
login_entry = Entry(width=21, font=FONT_ENTRY)
login_entry.grid(column=1, row=2)
login_entry.insert(0, STARTING_EMAIL)
password_entry = Entry(width=21, font=FONT_ENTRY)
password_entry.grid(column=1, row=3)

# BUTTONS
generate_password_button = Button(text="Generate Password", command=generate_password, width=18, font=FONT_BUTTONS)
generate_password_button.grid(column=2, row=3)
search_button = Button(text="Search Database", command=find_password, width=18, font=FONT_BUTTONS)
search_button.grid(column=2, row=1)
reset_email_button = Button(text="Reset Email", command=reset_email, width=18, font=FONT_BUTTONS)
reset_email_button.grid(column=2, row=2)
add_button = Button(text="Add", width=48, command=save_to_file, font=FONT_BUTTONS)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
