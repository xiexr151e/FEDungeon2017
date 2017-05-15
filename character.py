class character:
    def __init__(self, name, position, growthRate):
        self.name = name
        self.position = position
        self.growthRate = growthRate

class hero:
    def __init__(self, name, position, growthRate):
        self.character = character(name, position, growthRate)

class enemy:
    def __init__(self, character):
        self.character = character(name, position, growthRate)
