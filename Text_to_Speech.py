import pyttsx3 #importing the package pyttsx3 from the library
text_speech = pyttsx3.init() #initializing the library
answer = input("What do you want to convert into speech") #taking input from the user
text_speech.say(answer) #converting the text into speech
text_speech.runAndWait() ##running the task