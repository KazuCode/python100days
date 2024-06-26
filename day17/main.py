from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

q_list = []

for question in question_data:
    new_question = Question(question["text"], question["answer"])
    q_list.append(new_question)

quiz = QuizBrain(q_list)

while quiz.still_has_question():
    quiz.next_question()
quiz.goodbye_message()