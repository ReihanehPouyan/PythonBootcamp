print(''' _                                     
| |                                    
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ 
| __| '__/ _ \/ _` / __| | | | '__/ _ |
| |_| | |  __/ (_| \__ \ |_| | | |  __/
 \__|_|  \___|\__,_|___/\__,_|_|  \___|\n\n''')

print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
decision1 = input("Choose your path. Turn to the left or to the right. Type 'left' or 'right'\n").lower()
if decision1 == "left":
    decision2 = input("You have to cross the river. Do you want swim or wait for a boat? Type 'swim' or 'wait'\n").lower()
    if decision2 == "wait":
        decision3 = input("Choose the door: red, blue or yellow. Type 'red', 'blue' or 'yellow'\n").lower()
        if decision3 == "red":
            print("Burned by fire. Game over!")
        elif decision3 == "blue":
            print("Eaten by a warm. Game over!")
        else:
            print("You are win! Take an icecream!")
    else:
        print("You was attacked by shark. Game over!")
else:
    print("Fall into a hole. Game over!")

