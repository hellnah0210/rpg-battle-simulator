from .character import Character

class Enemy(Character):
    def __init__(self,name,health,attack_damage,enemy_type): 
        super().__init__(name,health,attack_damage)
        self.enemy_type = enemy_type

