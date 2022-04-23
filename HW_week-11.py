'''
1) If you haven't finished the even/odd function, please take your time to finish it.
Or
2)extra credit (only if you wish)  Write a "guess number function": 1)  Let python generate a random number between 0 to 10. 2) let users input their guess. 3) if the user guesses right, print " Congratulations ! You win !"; if the user guesses wrong, print " try again".
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
 
