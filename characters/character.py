
class Character:
    def __init__(self,name,health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def show_status(self):
        print(f"Name: {self.name} - HP: {self.health} - Damage: {self.attack_power} ")

    def take_damage(self,amount):
        if amount >= 0 :
            new_health = self.health - amount
            if new_health < 0:
                new_health = 0
            self.health = new_health
            return self.health
        else:
            raise ValueError ("Invalid amount")

    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False

