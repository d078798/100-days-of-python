from data import question_data as qd
from question_model import question_model as qm
from quiz_brain import quiz_brain_model as qb

question_bank = []

for item in qd:
    q_text = item["text"]
    q_ans = item["answer"]
    new_question = qm(q_text,q_ans)
    question_bank.append(new_question)
    
# print(question_bank[0].answer)

brain = qb(question_bank)

while brain.still_has_questions():
    brain.next_question()
    
print(f"You Scored {brain.score}/{len(question_bank)}")