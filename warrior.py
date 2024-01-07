class Warrior:
    health = 50
    alive = True
    attack = 5
    defense = 0
    vampirism = 0


class Knight(Warrior):
    attack = 7

class Army():
    def __init__(self):
        self.health = 0
        self.attack = 0
        self.poc = 0

    def add_units(self, x, poc):
        self.health = x().health
        self.attack = x().attack
        self.poc = poc


class Defender(Warrior):
    health = 60
    attack = 3
    defense = 2


class Vampire(Warrior):
    health = 40
    attack = 4
    vampirism = 50


def fight(unit_1, unit_2):
    while unit_1.alive and unit_2.alive:
        unit_2.health -= unit_1.attack - unit_2.defense
        unit_1.health += (unit_1.vampirism/100)*(unit_1.attack - unit_2.defense)
        unit_1.health -= unit_2.attack - unit_1.defense
        unit_2.health += (unit_2.vampirism/100)*(unit_2.attack - unit_1.defense)
        if unit_2.health <= 0:
            unit_2.alive = False
            return True
        elif unit_1.health <= 0:
            unit_1.alive = False
            return False

class Battle:
    def fight(self, army1, army2):
        hp2 = hp_army2_2 = 0
        while army1.poc > 0 and army2.poc > 0:
            hp1 = army1.health if hp2 == 0 else hp2
            hp_army2_1 = army2.health if hp_army2_2 == 0 else hp_army2_2
            while True:
                hp_army2_1 -= army1.attack
                if hp_army2_1 <= 0:
                    hp2 = hp1
                    hp_army2_2 = 0
                    army2.poc -= 1
                    break
                hp1 -= army2.attack
                if hp1 <= 0:
                    hp_army2_2 = hp_army2_1
                    hp2 = 0
                    army1.poc -= 1
                    break
        if army1.poc:
            return True
        else:
            return False

chuck = Warrior()
bruce = Warrior()
carl = Knight()
dave = Warrior()
mark = Warrior()
bob = Defender()
mike = Knight()
rog = Warrior()
lancelot = Defender()
eric = Vampire()
adam = Vampire()
richard = Defender()
ogre = Warrior()


print(fight(chuck, bruce))
print(fight(dave, carl))
print(fight(carl, lancelot))
print(fight(eric, chuck))

my_army = Army()
my_army.add_units(Knight, 3)
enemy_army = Army()
enemy_army.add_units(Warrior, 2)
my_army_2 = Army()
my_army_2.add_units(Knight, 1)
my_army_2.add_units(Warrior, 2)
enemy_army_2 = Army()
enemy_army_2.add_units(Knight, 3)

battle = Battle()

print(battle.fight(my_army, enemy_army))
print(battle.fight(my_army_2, enemy_army_2))