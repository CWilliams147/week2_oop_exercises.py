import random
class Character:
    def __init__(self, health, power, coins):
        self.health = health
        self.power = power
        self.coins = coins
    
    def alive(self):
        return self.health > 0

    def print_status(self):
        print("{} has {} health and {} power remaining.".format(self.name, self.health, self.power))
    
    def shadow_block(self, enemy):
        if random.random() < 0.1:
            self.health -= 1
            self.health -= enemy.power
            print("{} died." .format(shadow.name))
        else:
            print("Shadow dodged the attack")
            
    def whack_zom(self, enemy):
        print("You did literally nothing, it's a zombie")

    def attack_vader(self, enemy):
        print("{}'s webs did nothing and he was lightsabered in half" .format(hero.name))

#==================================================================================

#Where I was gonna put the store class

#==================================================================================

class Hero(Character):
    def __init__(self, name, health, power, coins):
        self.name = name
        self.health = health
        self.power = power
        self.coins = coins

#self.power is subtracting whatever its value is from enemy
    def attack(self, enemy):
        double_damage_chance = 0.2
        if random.random() < double_damage_chance:
            damage = self.power * 2
        else:
            damage = self.power
        enemy.health -= self.power
        print("{} does {} damage to the {}.".format(hero.name, self.power, type(enemy).__name__))
        if enemy.health <= 0:
            print("The {} is dead.".format(enemy.name))

    def buy(self, item_cost):
        if self.coins >= item_cost:
            self.coins -= item_cost
            print("You bought the item! Remaining coins: {}".format(self.coins))
        else:
            print("Not enough coins to buy the item.")

#==================================================================================

class Shadow(Character):
    def __init__(self, name, health, power, bounty):
        self.name = name
        self.health = health
        self.power = power
        self.bounty = bounty
    
#==================================================================================
    
class Goblin(Character):
    def __init__(self, name, health, power, bounty):
        self.name = name
        self.health = health
        self.power = power
        self.bounty = bounty

    def attack(self, enemy):
        enemy.health -= self.power
        print("The {} does {} damage to you.".format(goblin.name, self.power))
        if enemy.health <= 0:
            print("You are dead.")

#==================================================================================

class Zombie(Character):
    def __init__(self, name, health, power, bounty):
        self.name = name
        self.health = health
        self.power = power
        self.bounty = bounty
    
#==================================================================================

class Darth_Vader(Character):
    def __init__(self, name, health, power, bounty):
        self.name = name
        self.health = health
        self.power = power
        self.bounty = bounty

#==================================================================================

class Red_Skull(Character):
    def __init__(self, name, health, power, bounty):
        self.name = name
        self.health = health
        self.power = power
        self.bounty = bounty

    def attack(self, enemy):
        enemy.health -= self.power
        print("The {} does {} damage to you.".format(red_skull.name, self.power))
        if enemy.health <= 0:
            print("You are dead.")

#==================================================================================

zombie = Zombie("The Zombie", 0, 0, 7)
shadow = Shadow("Shadow", 1, 0, 6)
hero = Hero("Spider-Man", 10, 5, 20)
goblin = Goblin("Green Goblin", 6, 2, 5)
vader = Darth_Vader("Darth Vader", 100, 100, 1000000)
red_skull = Red_Skull("Red Skull", 15, 0, 20)

#==================================================================================

def main():
    while goblin.alive() and hero.alive():
        print("------------------------------------")
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        print("The Hero has {} coins." .format(hero.coins))
        hero.print_status()
        goblin.print_status()
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        print("------------------------------------")
        print("What do you want to do?")
        print("1. Go Web Go")
        print("2. do nothing")
        print("3. Attack Shadow")
        print("4. Punch Red Skull")
        print("5. Whack Zombie")
        print("6. Attack Darth Vader")
        print("7. flee")
        print("> ", end="")
        user_input = input()
        if user_input == "1":
            # Call the attack method on the hero
            hero.attack(goblin)
            
        elif user_input == "2":
            # Call the attack method on the goblin
            goblin.attack(hero)
            pass
        elif user_input == "3":
            hero.shadow_block(shadow)
            pass
        elif user_input == "4":
            hero.attack(red_skull)
        elif user_input == "5":
            hero.whack_zom(zombie)
            pass
        elif user_input == "6":
            hero.attack_vader(vader)
            break
        elif user_input == "7":
            print("With great power comes great responsibility")
            break
        else:
            print("Invalid input {}".format(user_input))

main()