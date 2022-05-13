class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0  # keeps track of which question the user is currently on
        self.question_list = q_list

    # TODO Return a boolean value depending on the value of question_number.
    def still_has_questions(self):
        # return self.question_number < len(self.question_list)
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def next_question(self):
        # Retrieve the item at the current question_number from the question_list
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        # Use the input() function to show the user the Question text and ask for the user's answer
        user_answer = input(f"{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
        else: 
            print("You got it wrong.")
        print(f"The correct answer was: {correct_answer}.")

