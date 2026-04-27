'#ex1/new_factories.py'
from ex0.factories import CreatureFactory
from .new_creatures import Sproutling, Bloomelle, Shiftling, Morphagon
from .new_creatures import Creature


class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Sproutling()

    def create_evolved(self) -> Creature:
        return Bloomelle()


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Shiftling()

    def create_evolved(self) -> Creature:
        return Morphagon()
