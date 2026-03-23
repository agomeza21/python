class GardenError(Exception):
    def __init__(self, message="Unknown garden error"):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message="Unknown plant error"):
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    if not plant_name[0].isupper():
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")


def test_watering_system(plants: list) -> None:
    print("Opening watering system")
    try:
        for plant in plants:
            water_plant(plant)
            print(f"Watering {plant}: [OK]")
    except PlantError as p:
        print(f"Caught  {type(p).__name__}: {p}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system")


def main() -> None:
    print("=== Garden Watering System ===")
    print("")
    valid_plants = ["Tomato", "Lettuce", "Carrots"]
    invalid_plants = ["Tomato", "lettuce"]
    print("Testing valid plants...")
    test_watering_system(valid_plants)
    print("")
    print("Testing invalid plants...")
    test_watering_system(invalid_plants)
    print("")
    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    main()
