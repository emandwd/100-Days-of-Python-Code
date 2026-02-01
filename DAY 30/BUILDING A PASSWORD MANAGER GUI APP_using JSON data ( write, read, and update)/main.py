from tkinter import * #import all the classes
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list) # shuffle the list --> mixes everything randomly so the password isn't predictable

    # Join the characters into one string
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
            "password": password

        }
    }

    if website.strip() == "" or email.strip() == "" or password.strip() == "":
        messagebox.showwarning(title="Error", message="Please fill all fields")
    else:
            # The .get() function in Tkinter is used to retrieve the current value (text) from an input widget
            try:
                with open("data.json", "r") as data_file:
                    # reading old data
                    data = json.load(data_file) # --> how to read --> type : # <class 'dict'>
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent= 4)
            else:
                # updating old data with new data
                data.update(new_data)

                with open("data.json", "w") as data_file:
                    # saving the updated data
                    json.dump(data, data_file, indent= 4) # --> how to write

            finally:
                website_entry.delete(0,END)  # 0 means: start deleting from the first character and the end : to delete until the last character.
                password_entry.delete(0, END)


"""
JSON (JavaScript Object Notation) is a format used to store and exchange data. It’s like a dictionary in Python but stored as a string.
| Operation        | Function                |
| ---------------- | ----------------------- |
| Read from file   | `json.load(file)`       |
| Write to file    | `json.dump(data, file)` |
| Read from string | `json.loads(string)`    |
| Write to string  | `json.dumps(data)`      |
"""
"""
    messagebox.askokcancel --> It returns a Boolean value: True if the user clicks "OK" and False if the user clicks "Cancel"
    | Dialog Type        | Returns                   |
    | ------------------ | ------------------------- |
    | `askokcancel()`    | `True` / `False`          |
    | `askyesno()`       | `True` / `False`          |
    | `askyesnocancel()` | `True` / `False` / `None` |
    | `askretrycancel()` | `True` / `False`          |
    | `showinfo()`       | `None`                    |
    | `showwarning()`    | `None`                    |
    | `showerror()`      | `None`                    |
"""
# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file :
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else :
            if website in data :
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(title="website", message=f"Email: {email}\nPassword: {password}")
            else:
                messagebox.showinfo(title = "Error", message=f"No details for {website} exists.")




# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx= 20, pady = 20) # Add padding around the whole window. This gives your widgets room to breathe.

canvas = Canvas(width= 200, height=200, highlightthickness = 0)
pass_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=pass_image) # This puts the image at coordinates (100, 100) on the canvas.
canvas.grid(row=0, column=1) # You need to pack or grid the canvas so it shows up in the window

#labels
website_label = Label(text="Website: ")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width= 41)
website_entry.grid(row=1, column=1, columnspan= 1, pady=3)
website_entry.focus()

email_entry = Entry(width= 60)
email_entry.grid(row=2, column=1, columnspan= 2, pady=3)
email_entry.insert(0, "emandawood@gmail.com")

password_entry = Entry(width= 41)
password_entry.grid(row=3, column=1, columnspan=1, pady=3)

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2, pady=3)

add_button = Button(text="Add", width=51, command=save)
add_button.grid(row=4, column=1, columnspan=2, pady=4)


search_button = Button(text="Search", width= 14, command= find_password)
search_button.grid(row=1,column=2 )


window.mainloop()