from tkinter import *
from tkinter import messagebox
import pyperclip
import json
# ---------------------------- SEARCH DATA ------------------------------- #


def search():
    website = website_input.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found")



    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["Password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}\nCopied to Clipboard")
            pyperclip.copy(password)
        else:
            messagebox.showinfo(title="Error", message=f"No saved data for {website}")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def password_gen():

    import random

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8,10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for letter in range(nr_letters)]
    password_symbols = [random.choice(symbols) for symbol in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for number in range(nr_numbers)]

    password = password_numbers + password_symbols + password_letters
    random.shuffle(password)

    passw = "".join(password)
    pyperclip.copy(passw)

    pass_input.delete(0, END)
    pass_input.insert(END, passw)
    messagebox.showinfo(title="Password Manager", message=f"Password: {passw} has been copied to clipboard")

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_input.get()
    email = user_input.get()
    password = pass_input.get()
    new_data = {
        website: {
            "email": email,
            "Password": password,
        }
    }

    if len(website) == 0  or len(password) == 0 or len(email) == 0:
        messagebox.showinfo(title="Missing Fields", message="Make sure to fill the missing fields")

    else:
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
            website_input.delete(0, END)
            pass_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

website_title = Label(text="Website")
website_title.grid(column=0, row=1)

user_title = Label(text="Email/Username")
user_title.grid(column=0, row=2)

password_title = Label(text="Password")
password_title.grid(column=0, row=3)

website_input = Entry(width=37)
website_input.focus()
website_input.grid(column=1, row=1)

user_input = Entry(width=55)
user_input.insert(END, "tariqbatayneh@hotmail.com")
user_input.grid(column=1, row=2, columnspan=2)

pass_input = Entry(width=37)
pass_input.grid(column=1, row=3)

password_generator = Button(text="Generate Password", command=password_gen)
password_generator.grid(column=2, row=3)

password_save = Button(text="Add", width=47, command=save)
password_save.grid(column=1, row=4, columnspan=2)

search = Button(text="Search", command=search, width=15)
search.grid(column=2, row=1)

window.mainloop()
