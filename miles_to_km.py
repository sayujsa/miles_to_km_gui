from tkinter import *


def calculate_kms():
    n = float(input_box.get())
    answer.config(text=n*1.609)


window = Tk()
window.minsize(500, 200)
window.title("Miles to KM Calculator")
window.config(padx=20, pady=20)

input_box = Entry()
input_box.config(width=15)
input_box.grid(column=1, row=0, columnspan=1, padx=20, pady=10)

miles = Label(text="Miles", font=("Ariel", 20, "bold"))
miles.grid(column=2, row=0, padx=20, pady=10)

is_equal = Label(text="is equal to", font=("Ariel", 10, "bold"))
is_equal.grid(column=0, row=1, padx=20, pady=10)

answer = Label(text="0", font=("Ariel", 10, "bold"))
answer.grid(column=1, row=1, padx=20, pady=10)

km = Label(text="KM", font=("Ariel", 10, "bold"))
km.grid(column=2, row=1, padx=20, pady=10)

button = Button(text="Calculate", command=calculate_kms)
button.grid(column=1, row=2, padx=20, pady=10)

window.mainloop()