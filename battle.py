import ex0


aqua_factory = ex0.AquaFactory()
flame_factory = ex0.FlameFactory()


def create_creatures(factory: ex0.CreatureFactory) -> None:
    base_creature = factory.create_base()
    evo_creature = factory.create_evolved()

    print(f"{base_creature.describe()}")
    print(f"{base_creature.attack()}")
    print(f"{evo_creature.describe()}")
    print(f"{evo_creature.attack()}")
    return


def battle_creature(factory1: ex0.CreatureFactory,
                    factory2: ex0.CreatureFactory) -> None:
    creature_1 = factory1.create_base()
    creature_2 = factory2.create_base()

    print(creature_1.describe())
    print(" vs.")
    print(creature_2.describe())
    print(" fight!")
    print(creature_1.attack())
    print(creature_2.attack())
    return


if __name__ == "__main__":
    test_factory = "Testing factory"
    test_battle = "Testing battle"
    print(f"\n{test_factory}")
    create_creatures(flame_factory)
    print(f"\n{test_factory}")
    create_creatures(aqua_factory)
    print()
    print(test_battle)
    battle_creature(flame_factory, aqua_factory)
