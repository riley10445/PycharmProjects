from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for entry in question_data:
    question_text = entry["text"]
    answer_text = entry["answer"]
    new_question = Question(question_text, answer_text)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

if not quiz.still_has_questions():
    print(
        f"You have completed the quiz! Your final score was {quiz.score}/{quiz.question_number}.\n")
