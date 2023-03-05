import tkinter
import tkinter.messagebox
import random
import pyperclip

# ---------------------------- CONSTANTS ------------------------------- #
FONT_NAME = "Courier"
FILE = "data.txt"
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# ---------------------------- ADD FUNCTION ------------------------------- #
def generate_password():
    password_letters = [random.choice(LETTERS) for _ in range(random.randint(8, 10))]
    password_numbers = [random.choice(NUMBERS) for _ in range(random.randint(2, 4))]
    password_symbols = [random.choice(SYMBOLS) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, tkinter.END)
    pyperclip.copy(password)
    password_entry.insert(0, password)
    print(password)


# ---------------------------- ADD FUNCTION ------------------------------- #
def add_password():
    website = website_entry.get()
    email_username = email_username_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(email_username) == 0 or len(password) == 0:
        warning_box = tkinter.messagebox.showwarning(
            message=f"Please fill all fields before proceeding.")
    else:
        msg = f"Website: {website}\nEmail: {email_username}\nPassword: {password}\nIs this ok?"
        msg_box = tkinter.messagebox.askokcancel(title="Password Manager", message=msg)

        if msg_box:
            with open(FILE, "a") as data:
                data.write(f"{website} | {email_username} | {password}\n")
                website_entry.delete(0, tkinter.END)
                password_entry.delete(0, tkinter.END)


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = tkinter.Canvas(width=200, height=200)
logo_img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
website_label = tkinter.Label(text="Website:")
website_label.grid(column=0, row=1)

email_username_label = tkinter.Label(text="Email/Username:")
email_username_label.grid(column=0, row=2)

password_label = tkinter.Label(text="Password:")
password_label.grid(column=0, row=3)

# Entries
website_entry = tkinter.Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2, sticky="EW")
website_entry.focus()

email_username_entry = tkinter.Entry(width=35)
email_username_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
email_username_entry.insert(0, "bernardoml@hotmail.com")

password_entry = tkinter.Entry(width=21)
password_entry.grid(column=1, row=3, sticky="EW")

# Buttons
generate_button = tkinter.Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3, sticky="EW")

add_button = tkinter.Button(text="Add", command=add_password, width=36)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")


window.mainloop()
