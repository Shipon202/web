questions = ("how many elements are in the periodic table : ",
             "which animal lays the largest eggs : ",
             "what is the most abundant gas in earth's atmosphere : ",
              "how many bones are in the human body : ",
            "which plant in the solar sytem is the hottest : ")

options = (("A. 116 ", "B. 117 ","C. 118 ","D. 119 "), 
           ("A. whale  ", "B. crocodile ","C. elephant ","D. ostrich "),
           ("A. Nitrogen ", "B. oxygen ","C. carbon ","D. hydrogen "),
           ("A. 206 ", "B. 207 ","C. 208 ","D. 209 "),
           ("A. mercury " , "B. vanus", "C. earth", "D. mars"))

answers = ("C", "D" , "A", "A", "B")
guesses = []

score = 0
question_num = 0


for question in questions:
    print("-----------------")
    print(question)
    for option in options[question_num]:
        print(option)
    
    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("correct")
    else:
        print("incorrect")
        print(f"{answers[question_num]} is correct answer")
    question_num += 1
print("-----Result-----")
print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guess: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()


score = int(score / len(questions) * 100)
print(f"your score is : {score}%")