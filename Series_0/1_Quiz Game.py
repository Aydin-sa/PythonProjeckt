"""
Quiz Game 

@author: Aydin Sasanian
"""

import sys

print("Welcome to my computer quiz! ")

playing = input("Do you want to play? ")

if playing.lower().strip() != "yes":
    print("Okay, maybe next time!")
    sys.exit()

print("Okay! Let's play :)")
score = 0

questions = {
    "What does CPU stand for? ": "central processing unit",
    "What does GPU stand for? ": "graphics processing unit",
    "What does RAM stand for? ": "random access memory",
    "What does PSU stand for? ": "power supply unit"
}

for question, correct_answer in questions.items():
    answer = input(question)
    if answer.lower().strip() == correct_answer:
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

total_questions = len(questions)
print(f"You got {score} out of {total_questions} questions correct!")
print(f"You got {round((score / total_questions) * 100)}%.")
