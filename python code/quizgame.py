questions = ("What is the capital of France?",
             "What is the capital of Germany?",
             "What is the capital of Italy?",
             "What is the capital of Spain?")

options = (("A.Paris", "B.Manilla", "C.Marseile", "D.Francia"),
           ("A.Bayern", "B.Berlin", "C.Dusseldorf", "D.Dormund"),
           ("A.Rome", "B.Turin", "C.Roma", "D.Sampdoria"),
           ("A.Lisbon", "B.Barcelona", "C.Seville", "D.Madrid"))
answers = ("A", "B", "A", "D")
guesses = []
score = 0
question_num = 0
for question in questions:
    print('-----------------------------------')
    print(question)
    print()
    for option in options[question_num]:
        print(option)
    guess = input("Enter your answer(A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        print('-----------------------------------')
        print("CORRECT!")
        score += 1
    else:
        print(f"INCORRECT! The correct answer is {answers[question_num]}")
    question_num += 1
    
score = int((score / len(questions))*100)    
print(f"Your current score is {score}%")    