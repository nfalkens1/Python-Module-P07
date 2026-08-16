from abc import ABC, abstractmethod


class Creature(ABC):
    """
    Abstract class to create creatures
    abstractmethod attack that creates and returns an attack
    describe returns a string (description of creature)
    """
    def __init__(self, name: str, type: str) -> None:
        self.name = name
        self.type = type
        super().__init__()

    @abstractmethod
    def attack(self) -> str:
        ...

    def describe(self) -> str:
        return f"{self.name} is a {self.type} type Creature"


class Flameling(Creature):
    def __init__(self) -> None:
        super().__init__("Flameling", "Fire")

    def attack(self) -> str:
        move = "Ember"
        return f"{self.name} uses {move}!"


class Pyrodon(Creature):
    def __init__(self) -> None:
        super().__init__("Pyrodon", "Fire/Flying")

    def attack(self) -> str:
        move = "Flamethrower"
        return f"{self.name} uses {move}!"


class Aquabub(Creature):
    def __init__(self) -> None:
        super().__init__("Aquabub", "Water")

    def attack(self) -> str:
        move = "Water Gun"
        return f"{self.name} uses {move}!"


class Torragon(Creature):
    def __init__(self) -> None:
        super().__init__("Torragon", "Water")

    def attack(self) -> str:
        move = "Hydro Pump"
        return f"{self.name} uses {move}!"
