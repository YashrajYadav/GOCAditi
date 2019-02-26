# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 14:36:17 2019

@author: Aditi
"""
import random
import matplotlib.pyplot as plt
import numpy as np
my_objects = []
class QA:
    def __init__(self,question,answer,question_level,question_marks,question_status):
        self.question=question
        self.answer=answer
        self.question_level=question_level
        self.question_marks=question_marks
        self.question_status=question_status
for i in range(1,50):
    my_objects.append(QA("Question from ques pool",random.choice(["a","b","c","d"]),random.choice(["low","mid","high"]),random.randint(1,14),True))
q_marks=0
scores=[]

def ask_question(level,marks):
    #print("-------------------------------")
    count=1
    for obj in my_objects:
        if obj.question_status==True:
            count=count+1
    print("-------------------------------")
    if count==40:
        return
    q_list=[]
    if level=="high":
        for obj in my_objects:
            if obj.question_level=="high" and obj.question_marks>marks and obj.question_status==True:
                q_list.append(obj)
    elif level=="low":
        for obj in my_objects:
            if obj.question_level=="low" and obj.question_marks<marks and obj.question_status==True:
                q_list.append(obj)
    elif level=="mid":
        for obj in my_objects:
            if obj.question_level=="mid" and obj.question_marks>marks and obj.question_status==True:
                q_list.append(obj)
    if(len(q_list)==0):
        q_list=random.choice(my_objects)
    #else:
        #print("size "+str(len(q_list)))
    question=random.choice(q_list)    
    print("Question Number: "+str(51-count))
    print()
    print(question.question)
    print("Correct answer: "+question.answer)
    print("Question level: "+question.question_level)
    print("Question marks: "+str(question.question_marks))
    question.question_status=False
    answer=input("Your answer\n")
    if level=="low":
        if answer==(question.answer):
            print("Correct")
            scores.append(question.question_marks)
            ask_question("mid",question.question_marks)
        else:
            print("Incorrect")
            scores.append(question.question_marks)
            if question.question_marks<3:
                ask_question("low",6)
            else:
                ask_question("low",question.question_marks)
    elif level=="mid":
        if answer==(question.answer):
            print("Correct")
            scores.append(question.question_marks)
            if question.question_marks>12:
                ask_question("high",9)
            else:
                ask_question("high",question.question_marks)
        else:
            print("Incorrect")
            scores.append(question.question_marks)
            if question.question_marks<3:
                ask_question("low",6)
            else:
                ask_question("low",question.question_marks)
    elif level=="high":
        if answer==(question.answer):
            print("Correct")
            scores.append(question.question_marks)
            if question.question_marks>12:
                ask_question("high",9)
            else:
                ask_question("high",question.question_marks)
        else:
            print("Incorrect")
            scores.append(question.question_marks)
            ask_question("mid",1)
try:
    name=input("Enter your name\n")
    mail=input("Enter your mail\n")
    ask_question("mid",0)
    print("Test complete")
    #print(scores)
    x=[1,2,3,4,5,6,7,8,9,10]
    plt.plot(x,scores)
    plt.xlabel('Question No-->')
    plt.ylabel('Marks-->')
   #plt.yticks(np.arange(0, 15, 1))
    plt.xticks(np.arange(0, 11, 1))
except:
    print("Sorry no questions left in the required category. Upload more questions to avoid this")