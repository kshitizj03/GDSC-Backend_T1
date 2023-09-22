from questionsdata import question_data
from quiz import Quiz

def main():
    quiz= Quiz(question_data)
   
    while quiz.questionremain():
        question=quiz.nextques()
        print(question.text)
        useranswer=input("Enter True/False:").strip().lower()
        if useranswer=="true":
            useranswer="True"
        elif useranswer=="false":
            useranswer="False"

        quiz.checkanswer(useranswer)
            
        if quiz.istimeup():
            print("Time's Up")
            
        else:
            print("Next Question Incoming..")

    print(f"Quiz Completed: Score is {quiz.score}")

main()
