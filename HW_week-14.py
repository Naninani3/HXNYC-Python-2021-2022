'''
Can you design a function for the user to guess the password? The user has 3 chances to guess. 
If user successed, please print 'Bingo'; If he/she fails to get this right in 3 times, print ; 'you are locked..'  (or anything you want to print =.=)
'''

def guess_password():

    password = "password"

   

    correct = False

    n = 0

   

    while (not correct and n < 3):

        user_guess = input("please guess the password, you have 3 chances: ")

        n = n+1

        if password == user_guess:

            correct= True

            print("Bingo!")

    if not correct:

        print("You're locked.")

   

guess_password()



 
