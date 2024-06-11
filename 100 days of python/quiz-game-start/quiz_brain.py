class quiz_brain_model():
    def __init__(self,question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
    
    def next_question(self):
        #print("Next Question")
        
        user_answer = input(f"Q{self.question_number +1}. {self.question_list[self.question_number].text} True/False: ")
        
        self.check_answer(user_answer)
        self.question_number += 1
    def still_has_questions(self):
        #print(self.question_number)
        number_of_questions = len(self.question_list)
        #print(number_of_questions)
        if self.question_number >= number_of_questions:
            print("NO MORE QUESTIONS")
            return False
        else:
            return True
    
    def check_answer(self,user_answer):
        user_answer = user_answer
        q_answer = self.question_list[self.question_number].answer
        
        if user_answer.lower() == q_answer.lower():
            self.score += 1
            print(f"Correct! \n Your Current Score is: {self.score}/{self.question_number+1}")
        else:
            print("Incorrect =[")
        
        print(f"The correct answer was: {q_answer}")
        
