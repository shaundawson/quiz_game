# TODO Bring question data into the main.py file. Instead of having a list of dictionaries, make a list of question objects.

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# TODO Create question_bank, a list of question objects
question_bank = []

# TODO Loop through ech of the questions in question_data
for question in question_data:
    #for each question create a variable called question_text
    question_text = question["text"]
    question_answer = question["answer"]
    # TODO Create a Question object from each entry in question_data
    new_question = Question(question_text,question_answer)
    # TODO Append each Question object to the question_bank
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz.next_question()
