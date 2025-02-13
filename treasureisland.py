print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1=input("where you want to go?type left or right: ")
if choice1 == "left":
    choice2=input("you will go next step? wait or swim :")
    if choice2 == "wait":
        choice3=input("the next step is! you can select the one color red,blue or yellow: ")
        if choice3 == "red":
            print("Burned by fire.Game Over.")
        elif choice3 == "blue":
            print("Eaten by beasts.Game Over.")
        elif choice3 == "yellow":
            print("you will win")
    else:
        print("Attacked by trout. game over")
else:
    print("Fall into a hole.Game over.")