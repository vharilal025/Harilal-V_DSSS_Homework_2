import random


def produce_random_integer(min_value, max_value):
    """
    Make a random integer in between min_value and max_value including those values.
    """
    return random.randint(min_value, max_value)


def choose_random_operator():
    """
    Choose any of the mathematical operations in addition or substraction or multiplication
    and return it.
    
    """
    return random.choice(['+', '-', '*'])


def make_maths_question(number1, number2, operator):
    """
    Make a maths question as string and return the correct answer with a string.
    """
    question = f"{number1} {operator} {number2}"
    if operator == '+': Answer = number1 + number2
    elif operator == '-': Answer = number1 - number2
    else: Answer = number1 * number2
    return question, Answer


def math_quiz():
    score = 0
    Total_score =5

    """
    Define a maths quiz using the input values and operations and finally shows a string
    with the final score in the game.
    
    """
    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(Total_score):
        number1 = produce_random_integer(1, 10)
        number2 = produce_random_integer(1, 5)
        operator = choose_random_operator()
        

        Problem, Answer = make_maths_question(number1, number2, operator)

        print(f"\nQuestion: {Problem}")
      
        # Handling invalid user input
        try:
            user_answer_input = int(input("Your answer: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue  # Skip the rest of the loop and move to the next question
            
        if user_answer_input == Answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {Answer}.")

    print(f"\nGame over! Your score is: {score}/{Total_score}")

if __name__ == "__main__":
    math_quiz()