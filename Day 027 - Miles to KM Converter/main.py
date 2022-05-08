from tkinter import *


def convert():
    result = float(user_input.get()) * 1.60
    result_label.config(text=result)


window = Tk()
window.title("Mile to KM Converter")
window.config(padx=20, pady=20)

# Entry
user_input = Entry(width=10,)
user_input.grid(column=1, row=0)
user_input.insert(END, string="0")

# Miles label
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

# is_equal to label
is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(column=0, row=1)

# result label
result_label = Label(text="0")
result_label.grid(column=1, row=1)

# KM label
km_label = Label(text="KM")
km_label.grid(column=2, row=1)

# calculate button
calculate_button = Button(text="Calculate", command=convert)
calculate_button.grid(column=1, row=2)


window.mainloop()
