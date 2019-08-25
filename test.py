import random

greeting_words={'hello','hey','hi','hola','greetings'}

greeting_response=['hello','welcome here','hey there']

def check_for_greeting(sentence):
    for word in sentence.split('  '):
        if word.lower() in greeting_words:
            return random.choice(greeting_response)
        else:
            return "try something else"

while True:
    sentence=input("You: ")
    response=check_for_greeting(sentence)
    print("bot:" + response)

    if 'bye' in sentence:
        break
