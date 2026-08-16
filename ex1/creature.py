from ex0.creature import Creature as Creature
from .capability import HealCapability, TransformCapability


class Sproutling(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__("Sproutling", "Grass")

    def attack(self) -> str:
        move = "Vine Whip"
        return f"{self.name} uses {move}!"

    def heal(self) -> str:
        heal = "heals itself for a small amount"
        return f"{self.name} {heal}"


class Bloomelle(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__("Bloomelle", "Grass/Fairy")

    def attack(self) -> str:
        move = "Petal Dance"
        return f"{self.name} uses {move}!"

    def heal(self) -> str:
        heal = "heals itself and others for a large amount"
        return f"{self.name} {heal}"


class Shiftling(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__("Shiftling", "Normal")

    def transform(self) -> str:
        self.transformed = True
        return f"{self.name} shifts into a sharper form!"

    def revert(self) -> str:
        self.transformed = False
        return f"{self.name} returns to normal."

    def attack(self) -> str:
        move = "attacks normally"
        b_move = "boosted strike"
        if self.transformed:
            return f"{self.name} performs a {b_move}!"
        else:
            return f"{self.name} {move}."


class Morphagon(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__("Morphagon", "Normal/Dragon")

    def transform(self) -> str:
        self.transformed = True
        return f"{self.name} morphs into a dragonic battle form!"

    def revert(self) -> str:
        self.transformed = False
        return f"{self.name} stabilizes its form."

    def attack(self) -> str:
        move = "attacks normally"
        b_move = "devastating morph strike"
        if self.transformed:
            return f"{self.name} unleashes a {b_move}!"
        else:
            return f"{self.name} {move}."
