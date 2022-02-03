import random 

number = random.randint(1, 9)
chances = 0

while chances < 5:
    guess = int(input("Enter Your Guess : "))

    if guess == number:
        print("Congratulations, YOU WON!")
        break
    else:
        print("Your guess is wrong, try Again")
        chances = chances + 1
     
if chances == 5:
    print("You Lost the Game!, the number was : "+str(number))