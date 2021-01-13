import random
import platform as p
class Dice:
    def __init__(self):
        self.faces = (1, 2, 3, 4, 5, 6)
    def roll(self):
        output = f'({random.choice(self.faces)}, {random.choice(self.faces)})'
        return output


d1 = Dice()
print(d1.roll())
print(p.system())
print(p.uname())
print(p.node())
