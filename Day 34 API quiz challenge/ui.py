THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain
class QuizInterface:
    def __init__(self, quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz 2.0")
        self.window.config(padx=20, pady=20,bg=THEME_COLOR)
        self.canvas = Canvas(width=300, height=250,bg="white")
        self.question_text = self.canvas.create_text(150,125,text='"This is a placeholder question?"',font=("Ariel 20 italic"),width = 300)
        self.canvas.grid(row=1, column=0,columnspan=2,pady=50)
        self.score = 0
        self.score_text = Label(text=f"Score:{self.score}",font=("Ariel","15"),fg="white",bg=THEME_COLOR,justify="center")
        self.score_text.grid(row=0,column=1)
        self.correct_img = PhotoImage(file=r"Day 34 API quiz challenge\images\true.png")
        self.false_img = PhotoImage(file =r"Day 34 API quiz challenge\images\false.png")
        self.true = Button(image=self.correct_img,highlightthickness=0,command=self.true_click)
        self.true.grid(row=2,column=0)
        self.false = Button(image=self.false_img,highlightthickness=0,command=self.false_click)
        self.false.grid(row=2,column=1)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.config(bg="white")
        self.canvas.itemconfig(self.question_text,text=q_text)
    
    def true_click(self):
        answer = "True"
        result = self.quiz.check_answer(answer)
        if result:
            self.score +=1
            self.canvas.config(bg="green")
            self.score_text.config(text=f"Score:{self.score}")
            self.canvas.update()
        else:
            self.canvas.config(bg="red")
            self.canvas.update()
        
        self.window.after(1000,self.get_next_question())

    
    def false_click(self):
        answer = "False"
        result = self.quiz.check_answer(answer)
        if result:
            self.score +=1
            self.score_text.config(text=f"Score:{self.score}")
            self.canvas.configure(bg="green")
            self.canvas.update()
        else:
            self.canvas.configure(bg="red")
            self.canvas.update()
        self.window.after(1000,self.get_next_question())