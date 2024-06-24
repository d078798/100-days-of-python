from tkinter import *
import pandas as pd
import random
import os

BACKGROUND_COLOR = "#B1DDC6"
KNOWN = []
UNKNOWN = []
RANDOM_WORDS = {}
FRENCH_DICT_LIST = []
SLEEP_TIME = 3

def endgame():
    canvas.delete()
    canvas.create_image(410,273,image=card_front_img)
    canvas.create_text(400,150,text="You have reached the end of the cards",font=("Ariel",30,"italic"))
    canvas.create_text(400,263,text=f"{len(KNOWN)}/{(len(KNOWN)+len(UNKNOWN))}", font=("Ariel",60,"bold"))
    canvas.update()

def show_english():
    
    word = RANDOM_WORDS["English"]
    canvas.delete()
    canvas.create_image(410,273,image=card_back_img)
    canvas.create_text(400,150,text="English",font=("Ariel",40,"italic"))
    canvas.create_text(400,263,text=word, font=("Ariel",60,"bold"))
    
    
def known_clicked():
    new_card(answer=True)
    
    

def unknown_clicked():
    new_card(answer=False)
    french_dataframe = pd.DataFrame.from_dict(UNKNOWN)
    pd.DataFrame.to_csv(french_dataframe,r"Day 31 flashcard project\data\words_to_learn.csv",index=False)

def new_card(answer):
    global RANDOM_WORDS
    global FRENCH_DICT_LIST
    global KNOWN
    global UNKNOWN
    global SLEEP_TIME, flip_timer
    
    if len(FRENCH_DICT_LIST) > 0:
        if answer == True:
            KNOWN.append(RANDOM_WORDS)
            FRENCH_DICT_LIST.remove(RANDOM_WORDS)
            print("known")
        
        if answer == False:
            UNKNOWN.append(RANDOM_WORDS)
            FRENCH_DICT_LIST.remove(RANDOM_WORDS)
            print("unknown")
        if len(FRENCH_DICT_LIST) > 0:
            RANDOM_WORDS = random.choice(FRENCH_DICT_LIST)
            french = RANDOM_WORDS["French"]
            english = RANDOM_WORDS["English"]
            canvas.delete()
            canvas.create_image(410,273,image=card_front_img)
            canvas.create_text(400,150,text="French",font=("Ariel",40,"italic"))
            canvas.create_text(400,263,text=french, font=("Ariel",60,"bold"))
            canvas.update()
            # show_english()
            print(KNOWN)
            print(UNKNOWN)
            flip_timer = window.after(3000,show_english)
            print(len(FRENCH_DICT_LIST))
        else:
            endgame()
    else:
        endgame()
    
    
    

# UI***************************************************************************

window = Tk()
window.title("Flash Card App")
window.configure(padx=50,pady=50,bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, show_english)

card_front_img = PhotoImage(file=r"Day 31 flashcard project\images\card_front.png")
card_back_img = PhotoImage(file=r"Day 31 flashcard project\images\card_back.png")
correct = PhotoImage(file=r"Day 31 flashcard project\images\right.png")
incorrect = PhotoImage(file=r"Day 31 flashcard project\images\wrong.png")



correct_button = Button(image=correct, highlightthickness=0,command=known_clicked)
incorrect_button = Button(image=incorrect, highlightthickness=0,command=unknown_clicked)

# Data reading
if os.path.exists(r"Day 31 flashcard project\data\words_to_learn.csv"):
    with open(r"Day 31 flashcard project\data\words_to_learn.csv","r") as f:
        french_dataframe = pd.read_csv(f)
else:
    with open(r"Day 31 flashcard project\data\french_words.csv","r") as f:
        french_dataframe = pd.read_csv(f)
    
FRENCH_DICT_LIST = pd.DataFrame.to_dict(french_dataframe,orient="records")

RANDOM_WORDS = random.choice(FRENCH_DICT_LIST)
french = RANDOM_WORDS["French"]
english = RANDOM_WORDS["English"]
canvas = Canvas(width = 810, height = 556,bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.create_image(410,273,image=card_front_img)
# canvas.create_text(400,150,text="French",font=("Ariel",40,"italic"))
# canvas.create_text(400,263,text=french, font=("Ariel",60,"bold"))

# language_label = Label(text="French",font=("Ariel",40,"italic"),fg="black")
# word = "test"
# word_label = Label(text=word, font=("Ariel",60,"bold"),fg="black")
# language_label.place(x=400,y=150)
# word_label.place(x=400,y=253)

canvas.grid(row=0,column=0, columnspan=2)
incorrect_button.grid(row=1, column=0,pady=10)
correct_button.grid(row=1, column =1,pady=10)

new_card("na")


# *****************************************************************************
window.mainloop()