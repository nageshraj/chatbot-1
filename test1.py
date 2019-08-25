import random
import sys

questions = ["how are you?",
             "whats up?",
             "what is up?",
             "what is your name?"]

answers =["i'm fine,thanks",
          "just chilling",
          "nothing much",
          "raj,naam toh suna hoga"]

def list_faq():
    for i in range(len(questions)):
        print(str(i)+":"+questions[i])
    print("\n")

def check_for_faq_by_index():
    list_faq()
    question_id=input("\nwhich question would you like to ask?")
    response=" "

    if "bye" in question_id:
        sys.exit()
    elif int(question_id)<len(questions):
        response=answers[int(question_id)]
    else:
        response="ask something else "
    return response

def check_for_faq(question):
    response=""
    if question in questions:
        index=questions.index(question)
        response=answers[index]
    else:
        response="ask something else"
    return response

while True:
    response=check_for_faq_by_index()
    print("bot:" +response)

