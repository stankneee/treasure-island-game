print('''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
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

left_right = input("You come to a fork in the road, do you go left or right?\n").lower()
if left_right == "left":
    print("You followed the road to the left and...")
    swim_wait = input("You reach a river, do you swim across or wait until a boat docks and ask for a ride?\n").lower()
    if swim_wait == "swim":
      print("You take the chance and swim across.")
      which_door = input("You reach a mysterious house with three colored doors, which door do you choose? Green, Red, or blue. \n").lower()
      if which_door == "red":
        print("You open the red door and find the treasure. You win!!! ")
      elif which_door == "blue":
        print("You open the blue door and are shocked to death at that very moment. Game over ")
      else:
        print("You open the green door and see a chest, you reach to open it and are poisoned. Game Over")
    else:
      print("You wait til midnight and board the strangers ferry and are taken to Hades... Game Over ")

else:
    print("You followed the right road and got hit by a wagon. Game Over")






