# Dragon Snax
# Aaran Rajadurai
# 08-02-2020 


print("You are in a dark room in a mysterios castle.")
print("Infront of you are three doors. You must choose one.")
playerChoice = input("Choose 1, 2 or 3...")

if playerChoice == 1:
    print("You find a room full of treasure. You're RICH!")
    print("GAME OVER, YOU WIN!")

elif playerChoice == 2:
    print(" The door opens and an angry ogre hits you with his club.")
    print("GAME OVER, YOU LOSE!")

elif playerChoice == 3:
    print("You go into the room and find a sleeping dragon.")
    print("You can either:")
    print("1) Try to steal some of the dragon's gold.")
    print("2) Try to sneak around the dragon to the exit.")
    dragonChoice = input("Type 1 or 2...")

    if dragonChoice == 1:
        print("The dragon wakes up and eats you. You are delicious.")
        print("GAME OVER, YOU LOSE!")
    elif dragonChoice == 2:
        print("You safely made it out without waking the dragon! FREEDOM!")
    else:
        print("Sorry, you didn't enter 1 or 2!")

else:
    print("Sorry, you didn't enter 1, 2 or 3!")

