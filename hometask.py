from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

class Sword(Weapon):
    def attack(self):
        return 'удар мечом'

class Bow(Weapon):
    def attack(self):
        return 'выстрел'

class Fighter:
    def __init__(self, weapon: Weapon):
        self.weapon = weapon

    def change_weapon(self, weapon: Weapon):
        self.weapon = weapon

    def attack(self):
        return f'боец наносит{self.weapon.attack()}'

class Monster():
    def __init__(self, health=100):
        self.health = health

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            return 'Монстр побежден'
        else:
            return f'у монстра осталось {self.health} здоровья'

def simulate_battle():
    sword = Sword()
    bow = Bow()

    fighter = Fighter(sword)
    monster = Monster()
    
    print()



