from tkinter import *

window = Tk()
window.title("Mile to KM converter")
# window.minsize(width=100,height=100)

# nothing, text input, label
# label,text output, label
# nothing, button, nothing

def button_clicked():
    miles_entered = floa(miles.get())
    km.configure(text="{:.2f}".format(miles_entered*1.609344))

miles = Entry()
miles_label = Label(text="Miles")

equal_to_label = Label(text="is equal to ")
km = Label(text="0")
km_label = Label(text="Km")

calc = Button(text="Calculate", command=button_clicked)


miles.grid(column = 1, row = 0)
miles_label.grid(column = 2, row = 0)
equal_to_label.grid(column = 0, row = 1)
km.grid(column = 1, row = 1)
km_label.grid(column = 2, row = 1)
calc.grid(column = 1, row = 2)
window.mainloop()