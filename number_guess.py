import random

number = random.randint(1, 100)

print("="*75 + "\nWelcome to the Number Guessing Game!\n"+"="*75)

print("You have selected a number between 1 and 100. Try to guess it!"+"\n\ngood luck!"+"\n")

chance = 5
print("You have", chance, "chances to guess the correct number.")

while True:
    try:
        INPUT = int(input("Enter your guess: "))
        break
    except ValueError:
        print("Please enter a whole number.")

while INPUT != number and chance > 0:
    if INPUT < number:
        print("Your guess is too low. Try again!")  
    elif INPUT > number:
        print("Your guess is too high. Try again!")
    else:
        print("Congratulations! You guessed the correct number!")

    chance -= 1
    INPUT = int(input("Enter your guess: "+"\nYou have " + str(chance) + " chances left: "))
   

if chance == 0:
    print("Sorry, you have run out of chances. The correct number was:", number)