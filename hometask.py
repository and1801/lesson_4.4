from abc import ABC, abstractmethod

# Абстрактный класс для оружия
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

# Конкретные классы оружия
class Sword(Weapon):
    def attack(self):
        return "удар мечом"

class Bow(Weapon):
    def attack(self):
        return "удар из лука"

# Класс бойца
class Fighter:
    def __init__(self, weapon: Weapon):
        self.weapon = weapon

    def change_weapon(self, weapon: Weapon):
        self.weapon = weapon

    def attack(self):
        return f"Боец наносит {self.weapon.attack()}."

# Класс монстра
class Monster:
    def __init__(self, health=100):
        self.health = health

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            return "Монстр побежден!"
        else:
            return f"У монстра осталось {self.health} здоровья."

# Демонстрация
def simulate_battle():
    sword = Sword()
    bow = Bow()

    fighter = Fighter(sword)
    monster = Monster()

    print("Боец выбирает меч.")
    print(fighter.attack())
    print(monster.take_damage(50))

    fighter.change_weapon(bow)
    print("\nБоец выбирает лук.")
    print(fighter.attack())
    print(monster.take_damage(50))

if __name__ == "__main__":
    simulate_battle()