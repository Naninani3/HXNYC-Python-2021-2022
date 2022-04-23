'''
Please Build a Number guessing game, in which the user can provide the guess and the program will guide user what the number is, 
by printing "your guess is high" or "your guess is low". (Feel free define how many times the user can guess，or user can guess  until he guess right)
''' 

def guess_number():

    number = 88

   

    correct = False

    n = 0

   

    user_guess = int(input("Please guess the number, you have 3 chances: "))

   

    while (not correct and n < 3):

        n = n+1

        if number == user_guess:

            correct= True

            print("Bingo!")

        elif 3-n>0:

            if number<user_guess:

                print("Your guess is too high")

            else:

                print("Your guess is too low")

            user_guess = int(input(f"You are incorrect, you have {3-n} chances remaining: "))

 

           

    if not correct:

        print("You lose!")

   

guess_number()
 
