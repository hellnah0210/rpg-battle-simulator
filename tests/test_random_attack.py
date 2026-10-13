from unittest.mock import patch
from characters import Character, Enemy
from battle import random_attack
import random

hero = Character("Knight", 120, 25)
enemy3 = Enemy("Goblin", 100, 10, "Monster")
chance = 0.2

with patch("battle.combat.random.random", return_value=chance):
    random_attack(hero, enemy3)
    
if chance < 0.2:
    assert enemy3.health == 50

    print("Critical Hit probability test passed!")
else:
    assert enemy3.health == 75

    print("Normal Hit probability test passed!")