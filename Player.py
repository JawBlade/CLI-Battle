import random

class Player:
    def __init__(self, name, health=100):
        self.name = name
        self.health = health
        self.move = {
            'attack': True,
            'defend': True,
            'heal'  : True
        }
    
    def attack(self):
        return random.randint(10,20)
    
    def defend(self):
        return True

    def heal(self):
        heal = self.health + 20
        if heal > 100:
            heal = 100
            self.health = heal
        return self.health

    def choice(self, move: str):
        return self.move.get(move, False)