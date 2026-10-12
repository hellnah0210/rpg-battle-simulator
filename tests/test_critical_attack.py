from characters import Character, Enemy
from battle import critical_attack

hero = Character("Knight", 120, 25)
enemy = Enemy("Goblin", 60, 10, "Monster")

critical_attack(hero, enemy)

assert enemy.health == 10
print("Critical Hit test passed!")