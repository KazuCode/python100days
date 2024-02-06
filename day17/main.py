import data, question_model, quiz_brain

q_list = []
number = 0

for entry in data.question_data:
    q_list.append(question_model.Question(entry['text'], entry['answer']))

quiz = quiz_brain.QuizBrain(q_list)
quiz.next_question()
