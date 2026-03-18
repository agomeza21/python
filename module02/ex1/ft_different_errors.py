def garden_operations() -> None:
    print("Testing ValueError...")
    try:
        temperature = "abc"
        temp = int(temperature)
    except ValueError as t:
        print(f"Caught {type(t).__name__}: {t}")
    print("")
    print("Testing ZeroDivisionError...")
    try:
        plants = 100
        sectors = 0
        sector_plants = plants / sectors
    except ZeroDivisionError as d:
        print(f"Caught {type(d).__name__}: {d}")
    print("")
    print("Testing FileNotFoundError...")
    try:
        open("text.txt")
    except FileNotFoundError as f:
        print(f"Caught {type(f).__name__}: {f}")
    print("")
    print("Testing KeyError...")
    try:
        flowers = {"tulip": "blue", "rose": "red"}
        flowers["sunflower"]
    except KeyError as e:
        print(f"Caught {type(e).__name__}: {e}")
    print("")
    print("Testing multiple errors toguether...")
    try:
        temperature = "abc"
        temp = int(temperature)
        plants = 100
        sectors = 0
        sector_plants = plants / sectors
    except (ValueError, ZeroDivisionError):
        print("Caught an error, but program continues!")

def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    print("")
    garden_operations()
    print("")
    print("All error types tested successfully!")


if __name__=="__main__":
    test_error_types()
