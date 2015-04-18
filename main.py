import random

###
# Testing guesses
def test(inputNum, answer, flag, lf, rt):
    # Running
    print("This is your guess: " + str(inputNum))
    if int(inputNum) == int(answer):
        print("You win the game!")
        return True
    else:
        print("You miss it. Please try for another guess.")
        return False
# End def
###


# Welcome message
print("Welcome to the guessing game!")

# Generate answer number, init variable
ans = random.randint(1, 100)
left = 1
right = 100
flag = False

# Ask for input
num = input("Please guess a number(1 - 100): ")

# Detect input error
while int(num) > 100 or int(num) < 1 :
    num = input(" Wrong number, please try different number: " )

while flag == False :
    flag = test( num , ans, flag, left, right)
    
    if flag == True:
        break
    else:
        # change range
        if ( ans < int(num) ):
            right = int(num)
        else:
            left = int(num)
        num = input("Please guess a number from " + str(left) + " to " + str(right) +" :")
        
