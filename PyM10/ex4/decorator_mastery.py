import functools
import time
from typing import Callable, Any


def spell_timer(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"Spell completed in {elapsed:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(self, spell_name: str, power: int) -> Any:
            if power < min_power:
                return "Insufficient power for this spell"
            return func(self, spell_name, power)
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print(f"Spell failed, retrying... (attempt {attempt}/{max_attempts})")
                    else:
                        print(f"Spell failed, retrying... (attempt {attempt}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and name.replace(" ", "").isalpha()

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


if __name__ == "__main__":
    print("Testing spell timer...")
    @spell_timer
    def fireball():
        time.sleep(0.1)
        return "Fireball cast!"
    print(f"Result: {fireball()}\n")

    print("Testing retrying spell...")
    @retry_spell(3)
    def failing_spell():
        raise RuntimeError("Spell failed!")
    result = failing_spell()
    print(f"{result}\n")

    print("Testing retrying success...")
    attempt_count = 0
    @retry_spell(3)
    def eventually_success():
        global attempt_count
        attempt_count += 1
        if attempt_count < 3:
            raise RuntimeError("Not yet!")
        return "Waaaaaaagh spelled !"
    print(eventually_success())

    print("\nTesting MageGuild...")
    guild = MageGuild()
    print(MageGuild.validate_mage_name("Gandalf"))
    print(MageGuild.validate_mage_name("Al"))
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Weak Spell", 5))
