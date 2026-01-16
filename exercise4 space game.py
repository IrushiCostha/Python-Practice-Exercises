#printing the greeting
print("Hello Space Traveller! Welcome to your journey of reach Planet X safely.")
print("You are at the Space Station")

#initiating veriables
first = str(input("Go 'Left' to the repair bay, or 'Right' to the launch pad."))

if first == "Left":
    print("You meet an alien")
    second = str(input("You can either 'Trust' him to fix your ship or 'Ignore' him."))
    if second == "Trust":
        print("The alien repairs your ship and gives you a star map.You safely reach Planet X. You win!")
    else:
        print("Your ship breaks down in space. Game Over.")
else:
    print("You reach the launch pad but your ship has no fuel.")
    third = str(input("Decide to 'Steal' fuel or 'Wait' for the station crew."))
    if third == "Wait":
        print("The crew helps you, and you travel safely to Planet X. You win!")
    else:
        print("You are caught and thrown into a black hole. Game Over.")
        
