from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


# TODO Create question_bank, a list of question objects
question_bank = []
still_has_questions = True

# TODO Loop through ech of the questions in question_data
for question in question_data:
    #for each question create a variable called question_text
    question_text = question["question"]
    question_answer = question["correct_answer"]
    # TODO Create a Question object from each entry in question_data
    new_question = Question(question_text,question_answer)
    # TODO Append each Question object to the question_bank
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

# TODO Use while loop to show the next question until the end
while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
    