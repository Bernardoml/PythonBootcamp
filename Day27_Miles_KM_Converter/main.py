import tkinter


def convert_m_to_km():
    miles = float(user_input.get())
    km = miles * 1.609
    result_label.config(text=f"{km}")


window = tkinter.Tk()
window.title("Miles to KM Converter")
window.minsize(width=100, height=100)
window.config(padx=20, pady=20)  # Put padding around the window

# Labels
miles_label = tkinter.Label(text="Miles", font=("Arial", 15, "bold"))
miles_label.grid(column=2, row=0)

is_equal_label = tkinter.Label(text="is equal to", font=("Arial", 15, "bold"))
is_equal_label.grid(column=0, row=1)

result_label = tkinter.Label(text="0", font=("Arial", 15, "bold"))
result_label.grid(column=1, row=1)

km_label = tkinter.Label(text="Km", font=("Arial", 15, "bold"))
km_label.grid(column=2, row=1)

# Button
button = tkinter.Button(text="Calculate", command=convert_m_to_km)
button.grid(column=1, row=3)

# Entry
user_input = tkinter.Entry(width=10)
user_input.grid(column=1, row=0)
user_input.focus()

window.mainloop()
