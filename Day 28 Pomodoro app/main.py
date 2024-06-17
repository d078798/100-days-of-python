
from tkinter import *
import math
import time
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
TIMER = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global REPS
    global TIMER
    tom_label.configure(text="Timer",font=(FONT_NAME,50,"bold"),fg=GREEN, bg= YELLOW)
    REPS = 0
    window.after_cancel(TIMER)
    
    canvas.itemconfig(timer_text,text="00:00")
    
# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global REPS
    check = "✔"
    new_text = ""
    print(REPS)
    # time_to_contdown = 5 * 60
    if REPS <= 7:
        if REPS%2 == 0 or REPS == 0:
            tom_label.configure(text="Work",fg=RED)
            print("work")
            time_to_contdown = WORK_MIN
        elif REPS == 1 or REPS == 3 or REPS == 5:
            # reps_corrected = REPS+1
            if REPS == 1:
                new_text = check
                
            elif REPS == 3:
                new_text = check + check
            else:
                new_text = check + check + check 
            tom_label.configure(text="Short Break", fg=GREEN)
            checks_label.configure(text=new_text)
            time_to_contdown = SHORT_BREAK_MIN
            print("short rest")
        elif REPS == 7:
            new_text = check + check + check + check
            checks_label.configure(text=new_text)
            tom_label.configure(text="Long Break", fg=GREEN)
            time_to_contdown = LONG_BREAK_MIN
            print("long rest")

        countdown(time_to_contdown*60)
        

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    global REPS
    global TIMER
    # print(count)
    mins = math.floor(count/60)
    secs = count%60
    if secs < 10:
        secs = f"0{secs}"
    
    canvas.itemconfig(timer_text, text=f"{mins}:{secs}")
    # canvas.itemconfig(timer_text,text=count)
    
    if count > 0:
       TIMER = window.after(1000,countdown,count-1)
    else:
        REPS += 1
        start_timer()
    
        


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.configure(padx=100,pady =50,bg=YELLOW)
window.title("Pomodoro")



canvas = Canvas(width = 200, height=224, bg=YELLOW, highlightthickness=0)
tom_img = PhotoImage(file=r"Day 28 Pomodoro app\tomato.png")
canvas.create_image(100,112,image=tom_img)
timer_text = canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,30,"bold"))
tom_label = Label(text="Timer",font=(FONT_NAME,50,"bold"),fg=GREEN, bg= YELLOW)
check = "✔"
checks_label = Label(text="",fg=GREEN,bg=YELLOW)

start_button = Button(text="Start",command=start_timer)
reset_button = Button(text="Reset",command=reset_timer)




tom_label.grid(column=1,row=0)
canvas.grid(column=1,row=1)
start_button.grid(column=0,row=2)
reset_button.grid(column=2,row=2)
checks_label.grid(column=1,row=3)

window.mainloop()