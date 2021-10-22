from Gladiator import *
import random

class Luk(Gladiator):
    def __init__(self):
        super("Arcus", 7,2,1000,20,random.randint(1,5),random.randint(1,3),random.randint(1,10)/10,random.randint(1,10)/10)
        self.maxHP
class MecAStit(Gladiator):
    def __init__(self):
        super("Gladius", 4,5,900,20,random.randint(1,5),random.randint(1,3),random.randint(1,10)/10,random.randint(1,10)/10)
class Jezdec(Gladiator):
    def __init__(self):
        super("Equus", 14,7,7000,20,random.randint(1,5),random.randint(1,3),random.randint(1,10)/10,random.randint(1,10)/10)
class Kopiník(Gladiator):
    def __init__(self):
        super("Hastatus", 8000,1,100,9,random.randint(5,6),random.randint(1,2),random.randint(1,10)/10,random.randint(1,10)/10)
