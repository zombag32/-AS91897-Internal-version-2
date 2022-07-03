from tkinter import *
from question_model import Question1
from quiz_data import question_data
from quiz_brain import QuizBrain
from quiz_ui import QuizInterface
from random import shuffle
import html
import sys
import tkinter as tk

def quit():
    sys.exit()
    
win = Tk() #creating an Tkinter frame
win.attributes("-fullscreen",True) # To make it full screen
win.title("Fun quiz main menu") #title of the window
Label(text="Welcome to fun quiz",bg="#1BB1D9", fg="white", font=("ariel", 60, "bold"),width=60).place(relx= 0.5, rely=0, anchor='n') #big title in the main menu
button = tk.Button(win, text = "Start", command= win.destroy, width = 15,bg="#1BB1D9", fg="white",font=("ariel",40,"bold"))#start button
button.place(relx=0.350,rely=0.3)

button2= tk.Button(win,text= "Quit", command= quit, width = 15,bg="#1BB1D9", fg="white",font=("ariel",40,"bold"))#quit button
button2.place(relx=0.350,rely=0.6)

Label(bg="#1BB1D9", fg="white",height=30,width=300).place(relx= 0.5, rely=0.9, anchor='n')#Label for bottom border for the main menu

win.mainloop()

#these codes will manage and link the other python scripts into one to form as my main quiz 
question_bank = []
for question in question_data:
    choices = []
    question_text = html.unescape(question["question"])
    correct_answer = html.unescape(question["correct_answer"])
    incorrect_answers = question["incorrect_answers"]
    for ans in incorrect_answers:
        choices.append(html.unescape(ans))
    choices.append(correct_answer)
    shuffle(choices)
    new_question = Question1(question_text, correct_answer, choices)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)

quiz_ui = QuizInterface(quiz)

#prints out the response and score to user
print("You have completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_no}")