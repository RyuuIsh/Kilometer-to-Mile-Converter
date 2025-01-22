from tkinter import *


def km_to_miles():
    km = float(km_input.get())
    miles = km / 1.609
    rounded_miles = round(miles, 2)
    miles_result_label.config(text=f"{rounded_miles}")


window = Tk()
window.title("Km to Mile Converter")
window.config(padx=20, pady=20)

km_input = Entry(width=7)
km_input.grid(column=1, row=0)

km_label = Label(text="Kilometer")
km_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

miles_result_label = Label(text=0)
miles_result_label.grid(column=1, row=1)

miles_label = Label(text="miles")
miles_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=km_to_miles)
calculate_button.grid(column=1, row=2)


window.mainloop()
