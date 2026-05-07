from collections.abc import Callable
from functools import reduce, partial, lru_cache, singledispatch
from typing import Any
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0
    if operation == "add":
        reduced_value = reduce(operator.add, spells)
    elif operation == "multiply":
        reduced_value = reduce(operator.mul, spells)
    elif operation == "max":
        reduced_value = reduce(lambda a, b: a if a > b else b, spells)
    elif operation == "min":
        reduced_value = reduce(lambda a, b: a if a < b else b, spells)
    else:
        raise ValueError(f"Unknown operation: {operation}")
    return reduced_value


def base_enchantment(power: int, element: str, target: str) -> str:
    return f"{element} enchantment hits {target} for {power}"


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    fire = partial(base_enchantment, 50, "fire")
    ice = partial(base_enchantment, 50, "ice")
    shadow = partial(base_enchantment, 50, "shadow")
    return {"fire": fire, "ice": ice, "shadow": shadow}


@lru_cache
def memoized_fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def dispacher(arg) -> str:
        return "Unknown spell type"

    @dispacher.register(int)
    def _(arg: int) -> str:
        return f"Damage spell: {arg} damage"

    @dispacher.register(str)
    def _(arg: str) -> str:
        return f"Enchantment: {arg}"

    @dispacher.register(list)
    def _(arg: list) -> str:
        return f"Multi-cast: {len(arg)} spells"

    return dispacher


def main() -> None:
    print("")
    spell_powers = [34, 45, 12, 34, 32, 12]
    operations = ['add', 'multiply', 'max', 'min']
    print("Testing spell reducer...")
    print(f"Sum: {spell_reducer(spell_powers, operations[0])}")
    print(f"Product: {spell_reducer(spell_powers, operations[1])}")
    print(f"Max: {spell_reducer(spell_powers, operations[2])}")
    print(f"Min: {spell_reducer(spell_powers, operations[3])}")
    print("")

    print("Testing partial_enchanter...")
    enchanters = partial_enchanter(base_enchantment)
    print(enchanters["fire"](target="Dragon"))
    print(enchanters["ice"](target="Knight"))
    print(enchanters["shadow"](target="Mage"))
    print("")

    print("Testing memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")
    print("")

    print("Testing spell dispatcher...")
    dispatch = spell_dispatcher()
    print(dispatch(42))
    print(dispatch("fireball"))
    spells = ["fireball", "dragon", "mage"]
    print(dispatch(spells))
    unknown = {"fireball": 7, "dragon": 4}
    print(dispatch(unknown))


if __name__ == "__main__":
    main()
