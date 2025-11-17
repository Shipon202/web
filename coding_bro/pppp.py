questions = (
    "How many elements are in the periodic table: ",
    "Which animal lays the largest eggs: ",
    "What is the most abundant gas in Earth's atmosphere: ",
    "How many bones are in the human body: ",
    "Which planet in the solar system is the hottest: "
)

options = (
    ("A. 116", "B. 117", "C. 118", "D. 119"),
    ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
    ("A. Nitrogen", "B. Oxygen", "C. Carbon", "D. Hydrogen"),
    ("A. 206", "B. 207", "C. 208", "D. 209"),
    ("A. Mercury", "B. Venus", "C. Earth", "D. Mars")
)

answers = ("C", "D", "A", "A", "B")
guesses = []

# Display all questions and options
print("----- Questions -----")
for question_num, question in enumerate(questions):
    print("-----------------")
    print(question)
    for option in options[question_num]:
        print(option)

# Collect guesses
print("\nPlease enter your guesses:")
for question_num in range(len(questions)):
    guess = input(f"Question {question_num + 1} (Enter A, B, C, D): ").upper()
    guesses.append(guess)

# Calculate score
score = 0
for question_num in range(len(questions)):
    if guesses[question_num] == answers[question_num]:
        score += 1
        print(f"Question {question_num + 1}: Correct")
    else:
        print(f"Question {question_num + 1}: Incorrect. The correct answer is {answers[question_num]}.")

# Display results
print("----- Result -----")
print("Answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("Guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score_percentage = int(score / len(questions) * 100)
print(f"\nYour score is: {score_percentage}%")