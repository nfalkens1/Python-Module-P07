import ex1


healing_factory = ex1.HealingCreatureFactory()
transform_factory = ex1.TransformCreatureFactory()
form = [" base:", " evolved:"]
header = ["Testing Creature with healing capability",
          "Testing Creature with transform capability"]


def test_healing(factory: ex1.HealingCreatureFactory) -> None:
    base_creature = factory.create_base()
    evo_creature = factory.create_evolved()
    print(header[0])
    print(form[0])
    print(base_creature.describe())
    print(base_creature.attack())
    print(base_creature.heal())
    print(form[1])
    print(evo_creature.describe())
    print(evo_creature.attack())
    print(evo_creature.heal())
    return


def test_transform(factory: ex1.TransformCreatureFactory) -> None:
    base_creature = factory.create_base()
    evo_creature = factory.create_evolved()
    print(header[1])
    print(form[0])
    print(base_creature.describe())
    print(base_creature.attack())
    print(base_creature.transform())
    print(base_creature.attack())
    print(base_creature.revert())
    print(form[1])
    print(evo_creature.describe())
    print(evo_creature.attack())
    print(evo_creature.transform())
    print(evo_creature.attack())
    print(evo_creature.revert())
    return


if __name__ == "__main__":
    test_healing(healing_factory)
    print()
    test_transform(transform_factory)
