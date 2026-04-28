'#ex1/new_creatures.py'
from ex0.creature import Creature
from .capabilities import HealCapability, TransformCapability


class Sproutling(Creature, HealCapability):
    def __init__(self) -> None:
        self.name: str = "Sproutling"
        self.creature_type: str = "Grass"

    def attack(self) -> str:
        c_attack = "Vine Whip"
        return f"{self.name} uses {c_attack}!"

    def heal(self) -> str:
        return f"{self.name} heals itself for a small amount"


class Bloomelle(Creature, HealCapability):
    def __init__(self) -> None:
        self.name: str = "Bloomelle"
        self.creature_type: str = "Grass/Fairy"

    def attack(self) -> str:
        c_attack = "Petal Dance"
        return f"{self.name} uses {c_attack}!"

    def heal(self) -> str:
        return f"{self.name} heals itself and others for a large amount"


class Shiftling(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__()
        self.name: str = "Shiftling"
        self.creature_type: str = "Normal"
        self._state: bool = False

    def transform(self) -> str:
        self._state = True
        return f"{self.name} shifts into a sharper form!"

    def revert(self) -> str:
        self._state = False
        return f"{self.name} returns to normal."

    def attack(self) -> str:
        if self._state:
            return f"{self.name} performs a boosted strike!"
        return f"{self.name} attacks normally."


class Morphagon(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__()
        self.name: str = "Morphagon"
        self.creature_type: str = "Normal/Dragon"
        self._state: bool = False

    def transform(self) -> str:
        self._state = True
        return f"{self.name} morphs into a dragonic battle form!"

    def revert(self) -> str:
        self._state = False
        return f"{self.name} stabilizes its form."

    def attack(self) -> str:
        if self._state:
            return f"{self.name} unleashes a devastating morph strike!"
        return f"{self.name} attacks normally."
