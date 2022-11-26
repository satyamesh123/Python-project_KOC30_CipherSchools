import random
name = input("Enter your name: ")
print(">> Hello",name,", welcome to the quiz world. <<")
print(" ")
print("    -----------------------------------------------")
print(" ")
print("[Note: Give your response in 'T'(for True) or 'F'(for false) of the following quiz questions.]")
print(" ")
print("    ------------------------------------------------    ")
print(" ")
questions = {
    'q1' : "Q.: In Python, the % symbol is used for string formatting.",
    'q2' : "Q.: Python is an interpreted language.",
    'q3' : "Q.: In Python, the == operator is used for assignment.",
    'q4' : "Q.: Python is a case-sensitive language.",
    'q5' : "Q.: Python is a object-oriented language.",
    'q6' : "Q.: Australia is wider than the moon.",
    'q7' : "Q.: Canis lupus is a scientific name for a wolf.",
    'q8' : "Q.: The Battle of Hastings took place in 1066.",
    'q9' : "Q.: Tiger is the national animal of India.",
    'q10' : "Q.: Monaco is the smallest country in the world."
}
answers = {
    "q1" : "F",
    "q2" : "T",
    "q3" : "F",
    "q4" : "T",
    "q5" : "T",
    "q6" : "T",
    "q7" : "F",
    "q8" : "T",
    "q9" : "T",
    "q10" : "F"
}
score = 0
for i in range(5):
    q = random.choice(list(questions.keys()))
    print(questions[q])
    answer = input("Your answer: ")
    if answer == answers[q]:
        print("    >> Congrats , correct answer! <<")
        score += 1
        print("    -------------------------------------- ")
    else:
        print("    >> Incorrect answer <<")
        score += 0
        print("    -------------------------------------- ")
print(" ")
print("Total score obtained:",score)
