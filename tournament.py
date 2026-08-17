import ex2
import ex1
import ex0

healing_factory = ex1.HealingCreatureFactory()
transform_factory = ex1.TransformCreatureFactory()
fire_factory = ex0.FlameFactory()
aqua_factory = ex0.AquaFactory()
norm_strat = ex2.NormalStrategy()
def_strat = ex2.DefensiveStrategy()
agr_strat = ex2.AggressiveStrategy()


def battle(opponents: list[tuple[ex0.CreatureFactory,
                                 ex2.BattleStrategy]]) -> None:
    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            creature_1 = opponents[i][0].create_base()
            creature_2 = opponents[j][0].create_base()
            strategy_1 = opponents[i][1]
            strategy_2 = opponents[j][1]
            print()
            battle_header = "* Battle *"
            print(battle_header)
            print(creature_1.describe())
            print(" vs.")
            print(creature_2.describe())
            print(" now fight!")
            try:
                print(strategy_1.act(creature_1))
                print(strategy_2.act(creature_2))
            except ex2.InvalidStrategyError as e:
                print(f"Battle error, aborting tournament: {e}")
                return
    return


if __name__ == "__main__":
    t_header = "*** Tournament ***"
    t_0_header = "Tournament 0 (basic)"
    t_0_pool = [(fire_factory, norm_strat),
                (healing_factory, def_strat)]
    t_0_teamcount = len(t_0_pool)
    print(t_0_header)
    print(" [ (Flameling+Normal), (Healing+Defensive) ]")
    print(t_header)
    print(f"{t_0_teamcount} opponents involved")
    battle(t_0_pool)
    print()
    t_1_header = "Tournament 1 (error)"
    t_1_pool = [(fire_factory, agr_strat),
                (healing_factory, def_strat)]
    t_1_teamcount = len(t_1_pool)
    print(t_1_header)
    print(" [ (Flameling+Aggressive), (Healing+Defensive) ]")
    print(t_header)
    print(f"{t_1_teamcount} opponents involved")
    battle(t_1_pool)
    print()
    t_2_header = "Tournament 2 (multiple)"
    t_2_pool = [(aqua_factory, norm_strat),
                (healing_factory, def_strat),
                (transform_factory, agr_strat)]
    t_2_teamcount = len(t_2_pool)
    print(t_2_header)
    print(" [ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    print(t_header)
    print(f"{t_2_teamcount} opponents involved")
    battle(t_2_pool)
