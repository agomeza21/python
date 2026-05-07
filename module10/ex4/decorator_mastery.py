from collections.abc import Callable
from functools import wraps
import time


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs) -> str:
        print(f"Casting {func.__name__}...")
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        duracion = fin - inicio
        print(f"Spell completed in {duracion:.3f} seconds")
        return resultado
    return wrapper


@spell_timer
def fireball() -> str:
    time.sleep(0.1010)
    return "Fireball cast!"


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> str:
            power = args[-1]
            if power >= min_power:
                return func(*args, **kwargs)
            return "Insufficient power for this spell"
        return wrapper
    return decorator


@power_validator(20)
def cast_spell(power) -> str:
    return f"Spell cast with {power} power"


def retry_spell(max_attempts: int) -> Callable:
    def decorator2(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> str:
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception:
                    attempts += 1
                    if attempts < max_attempts:
                        print(f"Spell failed, retrying... "
                              f"(attempt {attempts}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator2


attempt_counter = {"count": 0}


@retry_spell(3)
def spell() -> str:
    attempt_counter["count"] += 1
    if attempt_counter["count"] < 3:
        raise Exception()
    return "Waaaaaaagh spelled!"


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) < 3:
            return False
        for c in name:
            if not (c.isalpha() or c == " "):
                return False
        return True

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        if power >= 10:
            return f"Successfully cast {spell_name} with {power} power"
        return "Insufficient power for this spell"


def main() -> None:
    print("Testing spell timer...")
    resultado = fireball()
    print(f"Result: {resultado}")
    print("")

    print("Testing power_validator...")
    resultado1 = cast_spell(50)
    print(resultado1)
    resultado2 = cast_spell(10)
    print(resultado2)
    print("")

    print("Testing retrying spell...")
    print("First call:")
    print(spell())
    print("Second call:")
    print(spell())
    print("")

    print("Testing MageGuild...")
    print(MageGuild.validate_mage_name("Gandalf"))
    print(MageGuild.validate_mage_name("x"))
    guild = MageGuild()
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Fireball", 5))


if __name__ == "__main__":
    main()
