import time
print("--------------------------------------------------")
#Welcome the user
print("Welcome to the Math Quiz Game!")
time.sleep(2)
print("--------------------------------------------------")

#Chances
chances=1
print("You have to pick", chances,"correct answer.\nYou will get 1 score if you pick a correct answer.\nUse capital letter to write your answer.\n")
time.sleep(4)

#score
score=0

#question 1
print("==================================================")
question_1=print("1) 10 + 9 - 2 x 2 = ?\n(A) 34\n(B) 15\n(C) 24\n\n")
answer_1= "b"

for i in range(chances):
    Answer = input("Answer: ")
    if (Answer.lower() == answer_1):
        print("CORRECT! GOOD JOB!\n")
        score = score + 1
        break
    else:
        print("INCORRECT!\n")
        time.sleep(1)
        print("THE CORRECT ANSWER IS", answer_1, "\n\n")

time.sleep(2)

#question 2
print("==================================================")
question_2 = print("2) 12 / (6-2) + 2 = ?\n(A) 5\n(B) 2\n(C) 4\n\n")  
answer_2 = "A"

for i in range(chances):
    Answer = input("answer: ")
    if (Answer == answer_2):
        print("CORRECT! GOOD JOB!\n")
        score = score + 1
        break
    else:
        print("INCORRECT!\n ")
        time.sleep(1)
        print("THE CORRECT ANSWER IS", answer_2, "\n\n")

time.sleep(2)

#question 3
print("==================================================")
question_3 =print("3)  3 x 2 - 5 + 5 x 3 = ?\n(A) -12\n(B) 18\n(C) 16\n\n")
answer_3= "C"

for i in range(chances):
    Answer = input("Answer: ")
    if (Answer == answer_3):
        print("CORRECT! GOOD JOB!\n")
        score = score + 1
        break
    else:
        print("INCORRECT!\n")
        time.sleep(1)
        print("THE CORRECT ANSWER IS", answer_3, "\n\n")

time.sleep(2)

#question 4
print("==================================================")
question_4 =print("4)  5 - 10 x 2 - 4 = ?\n(A) -19\n(B) -14\n(C) 11\n\n")
answer_4= "A"

for i in range(chances):
    Answer = input("Answer: ")
    if (Answer == answer_4):
        print("CORRECT! GOOD JOB!\n")
        score = score + 1
        break
    else:
        print("INCORRECT!\n")
        time.sleep(1)
        print("THE CORRECT ANSWER IS",answer_4, "\n\n")

time.sleep(2)

#question 5
print("==================================================")
question_5 =print("5)  13 - 3 x 12 + 6/3 = ?\n(A) 42\n(B) -118\n(C) -21\n\n")
answer_5= "C"

for i in range(chances):
    Answer = input("Answer: ")
    if (Answer == answer_5):
        print("CORRECT! GOOD JOB!\n")
        score = score + 1
        break
    else:
        print("INCORRECT!\n")
        time.sleep(1)
        print("THE CORRECT ANSWER IS", answer_5, "\n\n")

time.sleep(2)

#print the score
print("==================================================")
if score ==5:
    print ("Congratulations!. You got full scores 5/5. Well done!")
elif score > 1:
    print("Well done! Your Score was", score)
else:
    print("Better luck next time! Your score was",score)

#Goobye message
print("Thank you for playing the Music Quiz Game!")