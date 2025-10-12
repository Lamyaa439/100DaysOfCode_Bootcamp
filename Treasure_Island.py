print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You are at a cross road. where do you want to go?")
way = input("left or right?\n")
if way == "right":
    print("Fall into a hole.\n Game Over.")
elif way == "left":
    print('''
                                                    ____
                                         v        _(    )
        _ ^ _                          v         (___(__)
       '_\V/ `
       ' oX`
          X                            v
          X             -HELP!
          X                                                 .
          X        \O/                                     /|
          X.a##a.   M                                     /_|
       .aa########a.>>                                    __|__
    .a################aa.                                 \   /
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~''')
    print("You've come to a lake.\n There is an island in the middle of the lake.")
    cross = input("Type (wait) to wait for a boat.\n Type (swim) to swim across.\n ")
    if cross == "swim":
        print("Attacked by trout. Game Over.")
    elif cross == "wait":
        print('''__________
                |  __  __  |
                | |  ||  | |
                | |  ||  | |
                | |__||__| |
                |  __  __()|
                | |  ||  | |
                | |  ||  | |
                | |  ||  | |
                | |  ||  | |
                | |__||__| |
                |__________|''')
        print("You arrive at the island unharmed. There is a house with 3 doors.\n")
        door = input("one red, one yellow and one blue. Which colour do you choose?\n")
        if door == "red":
            print("Burned by fire. Game Over.")
        elif door == "blue":
            print("Eaten by beasts. Game Over.")
        elif door == "yellow":
            print("You found the treasure. You Win !")
            print('''
   .-'"'-.
   / #     \
  : #       :  .-'"'-.
   \       /  / #     \
    \     /  : #       :
jgs  `'q'`    \       /
       (       \     /
        )       `'p'`
       (          )
        )        (
                  )''')
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("Game Over.")
else:
    print("Game Over.")

