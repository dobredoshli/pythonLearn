import random
while True:
    try:
        numberStr = input("Enter first number: ")
        number1 = int(numberStr)    
        number2Str = input("Enter second number: ")
        number2 = int(number2Str)

        if number2 < number1 or number1 == number2:
            raise ValueError("Second number should be greater than or equal to the first number")

        randomNumber = random.randint(number1, number2)  

        while True:
            guessStr = input("Your Guess (or 'exit' to end the game): ")

            if guessStr.lower() == 'exit':
                print(f"The number was {randomNumber}. Goodbye!")
                exit()

            guess = int(guessStr)

            if guess == randomNumber:
                print("Well Done, you guessed the number!")
                break
            else:
                print("Unfortunately no, try again")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {type(e).__name__} - {e}")

    

