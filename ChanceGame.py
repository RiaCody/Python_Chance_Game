import random

def introduction():
    print("Welcome to the Chance!")
    print("Are you ready to embark on a journey filled with excitement which will test you to the breaking point..")
    print("Make wise choices to see where you land and survive to succeed!\n")

def choose_path():
    print("You are walking into a deep forest and come across a dividing path. You can go 'left' or 'right'.")
    path = input("Which path do you dare to choose? (left/right): ").lower()
    return path

def encounter_monster():
    monsters = ["goblin", "troll", "dragon"]
    monster = random.choice(monsters)
    print(f"You encounter a deadly {monster}!")
    action = input("Do you 'fight' or 'run'? ").lower()
    
    if action == "fight":
        fight_monster(monster)
    elif action == "run":
        print(f"You run away safely! While hearing the {monster} behind you")
    else:
        print(f"Bad choice. The {monster} attacks you, and you barely escape with your life.")

def fight_monster(monster):
    print(f"You bravely decide to fight the {monster}!")
    player_health = 10
    monster_health = random.randint(5, 15)
    
    while player_health > 0 and monster_health > 0:
        print(f"Your health: {player_health}")
        print(f"{monster.capitalise()}'s health: {monster_health}")
        
        action = input("Do you want to 'attack' or 'defend'? ").lower()
        if action == "attack":
            damage = random.randint(1, 5)
            monster_health -= damage
            print(f"You hit the {monster} for {damage} damage!")
        elif action == "defend":
            print("You defend against the next attack.")
        else:
            print("Bad choice. You lose your turn.")

        if monster_health > 0:
            damage = random.randint(1, 5)
            player_health -= damage
            print(f"The {monster} hits you for {damage} damage!")

    if player_health > 0:
        print(f"You defeated the {monster}!\n")
    else:
        print(f"You were defeated by the {monster}...\n")

def find_treasure():
    treasures = ["gold coins", "lots of shiny gems", "an ancient artifact"]
    treasure = random.choice(treasures)
    print(f"You find {treasure}! Congratulations!\n")
    return treasure

class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = []

    def add_to_inventory(self, item):
        self.inventory.append(item)
        print(f"{item} has been added to your inventory.\n")

    def show_inventory(self):
        if self.inventory:
            print("Your inventory contains:")
            for item in self.inventory:
                print(f"- {item}")
        else:
            print("Your inventory is empty.")

def main():
    introduction()
    
    player_name = input("What is your name, brave adventurer: ")
    player = Player(player_name)
    
    while True:
        path = choose_path()
        
        if path == "left":
            encounter_monster()
        elif path == "right":
            treasure = find_treasure()
            add_item = input("Do you want to add this item to your inventory? (yes/no): ").lower()
            if add_item == "yes":
                player.add_to_inventory(treasure)
        
        player.show_inventory()
        
        continue_game = input("Do you want to continue your adventure? (yes/no): ").lower()
        if continue_game != "yes":
            break

    print("Thanks for playing the Chance Game!")

if __name__ == "__main__":
    main()
