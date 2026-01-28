import random

class characters:
    def __init__(self, name: str, health=100, color='white'):
        self.name   = name
        self.health = health
        self.color  = color
    
    def attack(self):
        return random.randint(10,20)
    
    def defend(self, damage):
        self.health -= damage // 2
        return True

    def heal(self):
        heal = self.health + 20
        if heal > 100:
            heal = 100
            self.health = heal
        return self.health