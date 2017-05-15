# A file that contains all classes for items

IS_WEAPON = True
NOT_WEAPON = False

'''
Superclass for item. This includes items and weapons.
'''
class item(self, name, isWeapon, dur):
    def __init__(self, name, isWeapon):
        self.name = name
        self.isWeapon = isWeapon

'''
Weapon class. Extends item.
'''
class weapon(self, name, dur, data):
    def __init__(self, name, dur, data):
        self.item = item(name, IS_WEAPON, dur)
        self.data = data

# TODO: Figure out whether I want to use tuples or arrays for item data.
#       Actually, use tuples for quick data access.
#       But I need a way to quickly access the tuples themselves
