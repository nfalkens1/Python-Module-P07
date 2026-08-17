from abc import ABC, abstractmethod
from ex0.creature import Creature
from ex1.capability import HealCapability, TransformCapability


class BattleStrategy(ABC):

    @abstractmethod
    def act(self, creature: Creature) -> str:
        ...

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        ...


class InvalidStrategyError(Exception):
    def __init__(self, message: str) -> None:
        self.message = message


class NormalStrategy(BattleStrategy):

    def act(self, creature: Creature) -> str:
        return creature.attack()

    def is_valid(self, creature: Creature) -> bool:
        return True


class AggressiveStrategy(BattleStrategy):

    def act(self, creature: Creature) -> str:
        if isinstance(creature, TransformCapability):
            build_out = (creature.transform(), creature.attack(),
                         creature.revert())
            format_out = "\n".join(build_out)
            return format_out
        else:
            raise InvalidStrategyError(f"Invalid Creature '{creature.name}'"
                                       " for this aggressive strategy")

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)


class DefensiveStrategy(BattleStrategy):

    def act(self, creature: Creature) -> str:
        if isinstance(creature, HealCapability):
            build_out = (creature.attack(), creature.heal())
            format_out = "\n".join(build_out)
            return format_out
        else:
            raise InvalidStrategyError(f"Invalid Creature '{creature.name}'"
                                       " for this defensive strategy")

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)
