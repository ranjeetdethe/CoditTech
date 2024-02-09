import time

def intro():
    print("Welcome to the Adventure Game: The Quest for the Enchanted Amulet!")
    print("You find yourself standing at a crossroads in the forest.")
    print("Your mission is to find the Enchanted Amulet hidden deep within the forest.")
    print("But beware, many dangers lie ahead!\n")

def crossroads():
    print("You are at the crossroads.")
    print("To your left, you see a dark cave entrance.")
    print("To your right, there is a narrow path leading into the dense forest.")
    print("What do you choose?")
    print("1. Enter the cave.")
    print("2. Take the narrow path through the forest.")
    choice = input("Enter your choice (1 or 2): ")
    if choice == "1":
        cave()
    elif choice == "2":
        forest()

def cave():
    print("\nYou enter the dark cave.")
    print("It's cold and damp, and you can hear the sound of dripping water echoing in the distance.")
    print("You see two tunnels branching off ahead.")
    print("What do you do?")
    print("1. Take the left tunnel.")
    print("2. Take the right tunnel.")
    choice = input("Enter your choice (1 or 2): ")
    if choice == "1":
        print("\nYou chose the left tunnel.")
        print("You encounter a pack of hungry wolves!")
        fight()
    elif choice == "2":
        print("\nYou chose the right tunnel.")
        print("You find a hidden chamber with a treasure chest!")
        print("Congratulations! You found the Enchanted Amulet!")
        print("You win!")
        replay()

def forest():
    print("\nYou venture into the dense forest.")
    print("The trees are so thick that barely any sunlight filters through.")
    print("You hear strange noises all around you.")
    print("You come across a river blocking your path.")
    print("What do you do?")
    print("1. Try to ford the river.")
    print("2. Look for a bridge or another way to cross.")
    choice = input("Enter your choice (1 or 2): ")
    if choice == "1":
        print("\nYou attempt to ford the river.")
        print("The current is too strong, and you get swept away!")
        print("Game over.")
        replay()
    elif choice == "2":
        print("\nYou search for another way to cross the river.")
        print("You find a rickety old bridge and cross safely to the other side.")
        print("You continue deeper into the forest.")
        print("You encounter a group of goblins blocking your path!")
        fight()

def fight():
    print("\nYou must fight the enemies to proceed!")
    player_health = 100
    enemy_health = 50
    while player_health > 0 and enemy_health > 0:
        print("\nPlayer Health:", player_health)
        print("Enemy Health:", enemy_health)
        print("1. Attack")
        print("2. Defend")
        choice = input("Enter your choice (1 or 2): ")
        if choice == "1":
            print("\nYou attack the enemy!")
            enemy_health -= 20
            print("Enemy takes 20 damage!")
        elif choice == "2":
            print("\nYou defend against the enemy's attack!")
            player_health -= 10
            print("You take 10 damage!")
        else:
            print("Invalid choice! Try again.")
            continue
    if player_health <= 0:
        print("\nYou have been defeated! Game over.")
        replay()
    elif enemy_health <= 0:
        print("\nYou defeated the enemies and continue on your quest!")
        print("You find the Enchanted Amulet!")
        print("Congratulations! You win!")
        replay()

def replay():
    choice = input("Do you want to play again? (yes/no): ")
    if choice.lower() == "yes":
        start_game()
    elif choice.lower() == "no":
        print("Thank you for playing!")
        exit()
    else:
        print("Invalid choice! Please enter 'yes' or 'no'.")
        replay()

def start_game():
    intro()
    crossroads()

start_game()
