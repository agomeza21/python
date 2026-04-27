'#ex0/creature.py'
from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self) -> None:
        self.name: str
        self.creature_type: str

    @abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> str:
        return f"{self.name} is a {self.creature_type} type Creature"


class Flameling(Creature):
    def __init__(self) -> None:
        self.name: str = "Flameling"
        self.creature_type: str = "Fire"

    def attack(self) -> str:
        c_attack = "Ember"
        return f"{self.name} uses {c_attack}!"


class Pyrodon(Creature):
    def __init__(self) -> None:
        self.name: str = "Pyrodon"
        self.creature_type: str = "Fire/Flying"

    def attack(self) -> str:
        c_attack = "Flamethrower"
        return f"{self.name} uses {c_attack}!"


class Aquabub(Creature):
    def __init__(self) -> None:
        self.name: str = "Aquabub"
        self.creature_type: str = "Water"

    def attack(self) -> str:
        c_attack = "Water Gun"
        return f"{self.name} uses {c_attack}!"


class Torragon(Creature):
    def __init__(self) -> None:
        self.name: str = "Torragon"
        self.creature_type: str = "Water"

    def attack(self) -> str:
        c_attack = "Hydro Pump"
        return f"{self.name} uses {c_attack}!"
