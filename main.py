from characters import Character,Enemy
from items import Inventory
from battle import attack

def main():
    print("=== RPG BATTLE ===")
    
    character = Character("Knight",100,20)
    enemy = Enemy("Goblin",60,10, "Monster")
    inventory = Inventory()

    inventory.add_item("Health Potion", 2)

    character.show_status()

    enemy.show_status()

    inventory.show_inventory()

    attack(character,enemy)
    attack(character,enemy)

    print("=== BATTLE FINISHED ===")

if __name__ == "__main__":
    main()