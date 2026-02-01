from tkinter import * #import all the classes
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
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

    if website.strip() == "" or email.strip() == "" or password.strip() == "":
        messagebox.showwarning(title="Error", message="Please fill all fields")
    else:
        is_ok = messagebox.askokcancel(title= website, message= f"These are the details entered: \nEmail: {email} "
                                                    f"\nPassword: {password}\nIs it ok to save?")
        if is_ok:
            # The .get() function in Tkinter is used to retrieve the current value (text) from an input widget
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END) # 0 means: start deleting from the first character and the end : to delete until the last character.
                password_entry.delete(0,END)


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
website_entry = Entry(width= 60)
website_entry.grid(row=1, column=1, columnspan= 2, pady=3)
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

window.mainloop()