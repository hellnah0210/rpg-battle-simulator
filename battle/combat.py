def attack(attacker, defender):
    # Lấy attack_power của attacker
    damage = attacker.attack_power
    # Gọi take_damage() của defender
    defender.take_damage(damage)
    # In thông báo chiến đấu
    print(f"{attacker.name} attacks {defender.name}!")
    print(f"{defender.name} HP: {defender.health} ")

def critical_attack(attacker,defender):
    damage = attacker.attack_power * 2
    defender.take_damage(damage)

    print(f"{attacker.name} lands a CRITICAL HIT on {defender.name}!")
    print(f"{defender.name} HP: {defender.health} ")
