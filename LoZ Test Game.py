import random
print ("Welcome, hero! Choose your item to start your adventure.")
print ("1. Sword")
print ("2. Bow")
print ("3. Hookshot")
choice = input("Enter the number of your choice: ")

if choice == '1':
    item = "Master Sword"
elif choice == '2':
    item = "Hero's Bow"
elif choice == '3':
    item = "Hookshot"
else:
    print("Invalid choice. You receive a wooden stick instead.")
    item = "Wooden Stick"

print(f"You have chosen the {item}! Your adventure begins now.")

# Random Enemy Encounter
enemies = ["Goblin", "Lizalfos", "Darknut", "Moblin"]
enemy = random.choice(enemies)
print(f"As you venture forth, a wild {enemy} appears!")

# Simple Combat Simulation
player_health = 100
enemy_health = 50
while player_health > 0 and enemy_health > 0:
    action = input("Do you want to (A)ttack or (R)un? ").upper()
    if action == 'A':
        damage = random.randint(10, 30)
        enemy_health -= damage
        print(f"You attack the {enemy} with your {item}, dealing {damage} damage!")
        if enemy_health <= 0:
            print(f"You have defeated the {enemy}! Victory is yours!")
            break
        enemy_damage = random.randint(5, 20)
        player_health -= enemy_damage
        print(f"The {enemy} attacks you back, dealing {enemy_damage} damage!")
        if player_health <= 0:
            print("You have been defeated. Game Over.")
            break
        print(f"Your health: {player_health}, {enemy}'s health: {enemy_health}")
    elif action == 'R':
        print("You run away safely. Adventure ends here.")
        break
    else:
        print("Invalid action. Please choose to (A)ttack or (R)un.")