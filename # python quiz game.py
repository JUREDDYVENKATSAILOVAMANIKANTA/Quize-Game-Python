# python quiz game

questions = ("What is the frist element in peridoic table?: ",
             "In which country the 2023 Asian Cup is gone to be held?: ",
             "What is the national bird of India?: ",
             "Which famous Indian cricketer is often referred to as the Master Blaster?:")

options = (("A.Hydrogen","B.Helium","C.Copper","D.Gold"),
           ("A.Pakisthan","B.Nepal","C.India","D.Bangladesh"),
           ("A.Peacock","B.Sparrow","C.Crow","D.Pigeon"),
           ("A.Rahul Dravid","B.Sourav Ganguly","C.Virat Kohli","D.Sachin Tendulkar"))

answers = ("A","C","A","D")
guesses = []
score = 0
question_num = 0 

for question in questions:
    print("-------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A,B,C,D):").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
            score += 1
            print("CORRECT!")
    else:
         print("INCORRECT!")
         print(f"{answers[question_num]} is the correct answer")
    question_num += 1     
print("-------------")
print("RESULTS")
print("-------------")

print("answers: ",end="")
for answer in answers:
     print(answer,end=" ")
print()
print("guesses: ", end="")
for guess in guesses:
     print(guess, end=" ")
print() 

score =int(score / len(questions) * 100)
print(f"Your score is:{score}")
            