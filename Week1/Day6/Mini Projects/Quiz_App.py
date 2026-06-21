# Features:
    # Ask questions
    # Check answers
    # Show score

name = input("Enter the player Name: ")

def Quiz():
    score = 0 
    
    print(f"\n--- Welcome to the Quiz, {name}! ---")

    
    print("\nQ1: What is the capital of Pakistan?")
    answer1 = input("Enter your Answer: ")
    if answer1.strip().lower() == "islamabad":
        print("Correct!")
        score += 1
    else:
        print("Incorrect Answer. The correct answer is Islamabad.")


    print("\nQ2: Which is the largest city of Pakistan by population?")
    answer2 = input("Enter your Answer: ")
    if answer2.strip().lower() == "karachi":
        print("Correct!")
        score += 1
    else:
        print("Incorrect Answer. The correct answer is Karachi.")


    print("\nQ3: What is the national sport of Pakistan?")
    answer3 = input("Enter your Answer: ")
    if answer3.strip().lower() == "hockey":
        print("Correct!")
        score += 1
    else:
        print("Incorrect Answer. The correct answer is Field Hockey.")


    print("\nQ4: Which mountain peak located in Pakistan is the 2nd highest in the world?")
    answer4 = input("Enter your Answer: ")
    if answer4.strip().upper() == "K2":
        print("Correct!")
        score += 1
    else:
        print("Incorrect Answer. The correct answer is K2.")


    print("\nQ5: In which year did Pakistan win the Cricket World Cup?")
    answer5 = input("Enter your Answer: ")
    if answer5.strip() == "1992":
        print("Correct!")
        score += 1
    else:
        print("Incorrect Answer. The correct answer is 1992.")
        
        
    print("\n" + "="*30)
    print(f"QUIZ OVER, {name.upper()}!")
    print(f"Your Final Score is: {score} out of 5")
    print("="*30)

# Call the function to start the game
Quiz()