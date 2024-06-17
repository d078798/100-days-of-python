import tkinter
from tkinter import *
# window = tkinter.Tk()
# window.title("tkintergui")
# window.minsize(width=500,height=300)

# #creating a label
# my_label = tkinter.Label(text="I am a label",font=("Arial",25,"bold"))
# my_label.pack()




# window.mainloop()

# def add(*args,adding=0):
    
#     for n in args:
#         adding +=n
#     return adding

# adding = 0
# while True:
#     adding = add(2,3,5,4,2,58,45,21,53)
#     print(adding)

def button_clicked():
    print("Clicked!")
    my_label.config(text=f"{input.get()}")
    
    
    
window = tkinter.Tk()
window.title("tkintergui")
window.minsize(width=500,height=300)

#creating a label
my_label = tkinter.Label(text="I am a label",font=("Arial",25,"bold"))


# updating text of a label
my_label["text"] = "New Text"
my_label.config(text="New Text")

# creating button



button = tkinter.Button(text="Click me", command=button_clicked)

button_2 = tkinter.Button(text="New Button",command=button_clicked)

# text Entry
input = Entry(width=10)



# my_label.pack(side="left")
# my_label.place(x=0,y=0)
my_label.grid(column=0,row=0)
button.grid(column=1,row=1)
button_2.grid(column=2, row = 0)
input.grid(column=3,row=2)

window.mainloop()