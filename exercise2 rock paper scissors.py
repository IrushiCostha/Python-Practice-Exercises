#game - rock/paper/scissors
import random
#start
use = int(input("What do you choose?Type, \n0 for Rock\n1 for Paper\n2 for Scissors\n"))

com = random.randint(0,2)
print(f"Computer chose {com}")

if use == 0 and com == 1 or use == 1 and com == 2 or use == 2 and com == 0:
    print("You lose!")
elif use == 0  and com == 2 or use == 1 and com == 0 or use == 2 and com == 1:
    print("You Win!")
elif use == com:
    print("It's a draw!")
else:
    print("You entered a invalid number")
