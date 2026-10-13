from unittest.mock import patch
from characters import Character, Enemy
from battle import random_attack

hero = Character("Knight", 120, 25)

test_cases = [
    (0.1999, 50),
    (0.2, 75),
    (0.2001, 75)
]

for chance, expected_hp in test_cases:

    # Bước 1: Tạo Goblin mới
    enemy = Enemy("Goblin", 100, 10, "Monster")
    # Bước 2: Dùng patch() với chance
    with patch("battle.combat.random.random",return_value = chance):
    # Bước 3: Gọi random_attack()
        random_attack(hero,enemy)
    # Bước 4: Assert HP bằng expected_hp
    
    assert enemy.health == expected_hp
    print(f"Test passed: chance = {chance}")