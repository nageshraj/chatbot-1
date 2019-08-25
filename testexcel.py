import pandas as pd
import sys
import numbers

df=pd.read_excel('questions.xlsx',sheet_name=0)

questions=df['questions'].tolist()

answers=df['answers'].tolist()

print("hello! 0s and 1s at your service")
def list_faq():
    print('following are some of the common questions')
    for i in range(len(questions)):
        print(str(i)+":"+questions[i])

def check_for_faq_by_index():
    list_faq()
    question_id=input("\nwhich question would you like to ask?")
    response=" "
    if 'no' in question_id:
        sys.exit()

    while not in question_id.isdigit():
        print("cannot answer it right now,try later")
        text_file=open("questions.txt","a")
        text_file.write(question_id +"\n")
        text_file.close()
        question_id=input("another question?")
        response=""

        if 'no' in question_id:
          sys.exit()

    if 'bye' in question_id:
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
