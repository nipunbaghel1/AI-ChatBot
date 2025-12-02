#Rule based AI Python ChatBot Project

import datetime
import time

name= input("Welcome, Enter your name:  ")
presentHour= datetime.datetime.now().hour

if 5 <= presentHour <= 11:
    print("Good Morning",name)

elif 11 <= presentHour <= 17:
    print("Good Afternoon",name)

elif 17 <= presentHour <= 20:
    print("Good Evening",name)
else:
    print("Good night",name)

print("Hello! Welconw to Rule Based ChatBot.")
print("You Can ask me a basic question,Type 'Bye' to exit from the bot")

#ChatBot memory (Dictionary of responses)

responses = {
    "hello":"Hi, Welcome.How can I help You?",
    "how are you":" I am very fine. Thank you",
    "who are you":"I am smart Ai Chatbot.",
    "motivate me":"keep going. Every bug of your project makes you better developer",
    "happy":"Great to hear that",
}
#Makes/Function to get response of ChatBot

def getResponseofBot(userQuestion):
    userQuestion = userQuestion.lower()
    for eachkey in responses:
        if eachkey in userQuestion:
            return responses[eachkey]
        

    return "I am not able to tell that.I am learn that soon."

#Take your input
while True:
    userInput = input("Please ask your question:")
    reply = getResponseofBot(userInput)
    print("Bot Response :",reply)

    if "bye" in userInput.lower():
        break