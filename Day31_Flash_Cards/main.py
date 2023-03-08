import tkinter
import pandas
import random

# ---------------------------- CONSTANTS ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"


# ---------------------------- Remove Known Word From List Function ------------------------------- #
def known_word():
    global data_dict, current_card
    data_dict.remove(current_card)
    csv_data = pandas.DataFrame(data_dict)
    csv_data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


# ---------------------------- TURN CARD FUNCTION ------------------------------- #
def turn_card():
    canvas.config(bg=BACKGROUND_COLOR)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_image, image=card_back_img)


# ---------------------------- NEXT CARD FUNCTION ------------------------------- #
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(data_dict)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_image, image=card_front_img)
    flip_timer = window.after(3000, func=turn_card)


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Flash Card App 2k23")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

try:
    data = pandas.read_csv("data/words_to_learn.csv")
    data_dict = data.to_dict(orient="records")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
    data_dict = data.to_dict(orient="records")

current_card = {}
flip_timer = window.after(3000, func=turn_card)

canvas = tkinter.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = tkinter.PhotoImage(file="images/card_front.png")
card_back_img = tkinter.PhotoImage(file="images/card_back.png")
card_image = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)


# Buttons
unknown_button_img = tkinter.PhotoImage(file="images/wrong.png")
unknown_button = tkinter.Button(image=unknown_button_img, command=next_card, highlightthickness=0)
unknown_button.grid(column=0, row=2)

known_button_img = tkinter.PhotoImage(file="images/right.png")
known_button = tkinter.Button(image=known_button_img, command=known_word, highlightthickness=0)
known_button.grid(column=1, row=2)

next_card()

window.mainloop()
