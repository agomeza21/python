'#ex2/strategies.py'
from abc import ABC, abstractmethod
from ex0.creature import Creature
from ex1.capabilities import HealCapability, TransformCapability


class InvalidStrategyError(Exception):
    pass


class BattleStrategy(ABC):
    @abstractmethod
    def act(self, creature: Creature) -> str:
        pass

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, Creature)

    def act(self, creature: Creature) -> str:
        return creature.attack()


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature | TransformCapability) -> str:
        if self.is_valid(creature):
            res1 = creature.transform()
            res2 = creature.attack()
            res3 = creature.revert()
            return f"{res1}\n{res2}\n{res3}"
        else:
            raise InvalidStrategyError(f"Invalid Creature '{creature.name}' "
                                       "for this aggressive strategy")


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature | HealCapability) -> str:
        if self.is_valid(creature):
            res1 = creature.attack()
            res2 = creature.heal()
            return f"{res1}\n{res2}"
        else:
            raise InvalidStrategyError(f"Invalid Creature '{creature.name}' "
                                       "for this defensive strategy")
