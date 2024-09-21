import random


def guess_the_num():
    num_to_guess = random.randint(1,100)
    attempts = 0
    print("Welcome to the game!!")
    print("I have picked a number between 1 to 100 and guess it to win !!! ")



    while True:
        try:
            user_input = int(input("Enter the number you guess: "))
            attempts += 1

            if user_input < num_to_guess:
                print("too low! try again....")
            elif user_input > num_to_guess:
                print("too high! try again")
            else:
                print(f"congratulation! you nailed it right in {attempts} attemps....")
                break
        except:
            print ("please enter the valid number!!!")
  
guess_the_num()