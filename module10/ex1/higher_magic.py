from collections.abc import Callable


def spell1(target: str, power: int) -> str:
    return f"{target} takes {power} damage"


def spell2(target: str, power: int) -> str:
    return f"{target} heals {power} HP"


def is_conditional(target: str, power: int) -> bool:
    _ = target
    return power > 50


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(target: str, power: int) -> tuple[str, str]:
        result1 = spell1(target, power)
        result2 = spell2(target, power)
        return (result1, result2)
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified(target: str, power: int) -> str:
        new_power = power * multiplier
        return base_spell(target, new_power)
    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def caster(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        else:
            return "Spell fizzled"
    return caster


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence(target: str, power: int) -> list[str]:
        results = []
        for spell in spells:
            results.append(spell(target, power))
        return results
    return sequence


def main() -> None:
    print("")
    print("Testing spell combiner...")
    combined = spell_combiner(spell1, spell2)
    result = combined("Dragon", 10)
    print("Combined spell result:", result[0] + ", " + result[1])
    print("")

    print("Testing power amplifier...")
    original_power = 10
    normal_result = spell1("Dragon", original_power)
    amplified_spell = power_amplifier(spell1, 3)
    amplified_result = amplified_spell("Dragon", original_power)
    print(f"Original power: {normal_result}")
    print(f"Amplified power: {amplified_result}")
    print("")

    print("Testing conditional caster...")
    power1 = 40
    power2 = 80
    casted_conditional = conditional_caster(is_conditional, spell2)
    print(f"Test1: power is {power1}")
    result1 = casted_conditional("Dragon", power1)
    print(result1)
    print(f"Test2: power is {power2}")
    result2 = casted_conditional("Dragon", power2)
    print(result2)
    print("")

    print("Testing spell sequence...")
    spells = [spell1, spell2]
    sequence = spell_sequence(spells)
    result_sequence = sequence("Dragon", 10)
    print(result_sequence)


if __name__ == "__main__":
    main()
