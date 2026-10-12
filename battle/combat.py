def attack(attacker, defender):
    # Lấy attack_power của attacker
    damage = attacker.attack_power
    # Gọi take_damage() của defender
    defender.take_damage(damage)
    # In thông báo chiến đấu
    print(f"{attacker.name} attacks {defender.name}!")
    print(f"{defender.name} HP: {defender.health} ")