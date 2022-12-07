import tkinter


def calculate():
    convert = round(int(input_miles.get()) * 1.609344, 2)
    label_to.config(text=f"{convert}")


window = tkinter.Tk()
window.title("Mile to KM Converter")
window.config(pady=40, padx=40)

input_miles = tkinter.Entry()
input_miles.insert(0, "0")
input_miles.config(width=10)
input_miles.grid(column=1, row=0)

label_miles = tkinter.Label(text="Miles")
label_miles.grid(column=2, row=0)

label_equal = tkinter.Label(text="is equal to")
label_equal.grid(column=0, row=1)

label_to = tkinter.Label(text="0")
label_to.grid(column=1, row=1)

label_km = tkinter.Label(text="KM")
label_km.grid(column=2, row=1)

button = tkinter.Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)

window.mainloop()
