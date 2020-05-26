import random as r
def random():
    return r.randint(1,100)

def valid(x,r,p):
    if x >= 1 and x <= 100:
        check(x,r,p)
    else:
        print("Invalid Guess...Try again!")

def check(y,n,points):
    random_number = n
    
    if points > 1:
        if y != random_number:
            if y > random_number:
                print("Oops...that's larger value than the number.\nTry thinking a small number.")

                points-=1

                z = int(input("\nGuess again...\n"))

                valid(z,n,points)
            elif y < random_number:
                print("Oops...that's smaller value than the number.\nTry thinking a larger number.")

                points-=1

                z = int(input("Guess again...\n"))

                valid(z,n,points)
    else:
        if points == 1:
            print("Sorry mate...Better luck next time")

            print("\nYOUR LUCK PERCENTAGE is 0%")

            print("\nThe random number was {}".format(random_number))
        else:
            print("That's correct!\n")

            print("CONGRATULATIONS!!!\n")

            level(points)

def level(score):
    LUCK_PERCENTAGE = score * 20
    if score == 1:
        print("Your score is {}".format(score))

        print("\nLEVEL-BEGINNER")

        print("YOUR LUCK PERCENTAGE is {}%".format(LUCK_PERCENTAGE))
    elif score > 1 and score < 5:
        print("Your score is {}".format(score))

        print("\nLEVEL-AMATEUR")
        
        print("YOUR LUCK PERCENTAGE is {}%".format(LUCK_PERCENTAGE))
    else:
        print("Your score is {}".format(score))

        print("\nLEVEL-CHAMPION")
        
        print("\nYOUR LUCK PERCENTAGE is {}%".format(LUCK_PERCENTAGE))
def main():
    print("WELCOME TO THE GUESSING GAME!\n\nPOINTS--05\n")
    
    print("Rules:\n1. You have to guess a Number between 1 and 100\n2. You have got 5 chances to do so.\n3. GOOD LUCK!")
    
    print("\nLet's START!\n")
    
    print("GUESS A NUMBER BETWEEN 1 and 100...\n")
    
    random_number = random()
    
    guess = int(input())

    points = 5

    valid(guess,random_number,points)
    
if __name__=="__main__":
    main()
