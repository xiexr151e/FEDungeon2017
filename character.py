# A file that defines all the character classes, including fighters and NPCs
import abc

# Global constants
HP_IND = 0
STR_IND = 1
MAG_IND = 2
SKL_IND = 3
SPD_IND = 4
LUK_IND = 5
DEF_IND = 6
RES_IND = 7

# The character class only has a name, a spawn location, and an icon.
class Character:

    def __init__(self, name, position, icon):
        self.name = name
        self.position = position


# The NPC class doesn't do anything special at this point.
# Shopkeeping and etc will be implemented later.
class NPC:
    def __init__(self, name):
        self.Character = Character(name, position, icon)

# The fighter class is an abstract class for the hero and the enemy.
# Contains everything both a hero and an enemy can do.
class Fighter:

    def __init__(self, name, position, growthRate, base, icon):

        # Delegate to superclass ctor
        self.Character = Character(name, position, icon)

        # Assign and initialize some attributes
        self.level = 1
        self.growthRate = growthRate
        self.setStats(base)

    def levelUp(self):

    def setStats(self, base):
        self.maxHP = self.HP = base[HP_IND]
        self.strength = base[STR_IND]
        self.magic = base[MAG_IND]
        self.skill = base[SKL_IND]
        self.speed = base[SPD_IND]
        self.defense = base[DEF_IND]
        self.resist = base[RES_IND]


# A hero class.
class Hero:
    def __init__(self, name, position, growthRate, base, icon):

        # Delegate to superclass ctor
        self.Fighter = Fighter(name, position, growthRate, base, icon)

        # Initialize stuff
        self.EXP = 0
        self.initialize()

    def initialize(self):
        '''
        Initialize the hero.
        '''


# An enemy class.
class Enemy:
    def __init__(self, name, position, growthRate, base, icon, floorNumber):

        # Deletegate to superclass ctor
        self.Fighter = Fighter(name, position, growthRate, icon)
        
        self.initialize(floorNumber)

    def initialize(self, floorNumber):
        '''
        Initialize the enemy based on current floor.
        '''

        # Based on floor number, level up this many times
        for levelTime in range(floorNumber):
            self.Fighter.levelUp()


