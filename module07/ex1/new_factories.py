'#ex1/new_factories.py'
from ex0.factories import CreatureFactory
from .new_creatures import Sproutling, Bloomelle, Shiftling, Morphagon


class HealingCreatureFactory(CreatureFactory):
    def create_base(self):
        return Sproutling()

    def create_evolved(self):
        return Bloomelle()


class TransformCreatureFactory(CreatureFactory):
    def create_base(self):
        return Shiftling()

    def create_evolved(self):
        return Morphagon()
