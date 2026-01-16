#printing the greeting
print("Welcome to the Treasure Island! \nyour mission is to find the treasure \nyou are at a cross road.")
x = input('Where do you want to go? Type "Left" or "Right": ').lower()

#level 1
if x == 'left':
    print('You come to a lake. There is an island in the middle of the lake.')
    y = input('Type "Wait" to wait for a boat. Type "Swim" to swim across').lower()

#level 2
    if y == 'wait':
        print('You arrive at the island unharmed. There is a house with  doors. red,yellow & blue.')
        z = input('Which color do you choose? ').lower()

#level 3
        if z == 'red':
            print('Burned by fire. Game Over')
        elif z == 'blue':
            print('Eaten by beasts. Game Over')
        elif z == 'yellow':
            print('You win')
        else:
            print('Game Over')
    else:
        print('Attacked by trout. Game Over')
else:
    print('Fall into a hole. Game Over')

