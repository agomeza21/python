class GardenError(Exception):
    def __init__(self, message="Unknown garden error"):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message="Unknown plant error"):
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message="Unknown water error"):
        super().__init__(message)


def check_plant() -> None:
    raise PlantError("The tomato plant is wilting!")


def check_water() -> None:
    raise WaterError("Not enough water in the tank!")


def main() -> None:
    print("=== Custom Garden Errors Demo ===")
    print("")
    print("Testing PlantError...")
    try:
        check_plant()
    except PlantError as p:
        print(f"Caught PlantError: {p}")
    print("")
    print("Testing WaterError...")
    try:
        check_water()
    except WaterError as w:
        print(f"Caught WaterError: {w}")
    print("")
    print("Testing catching all garden errors...")
    try:
        check_plant()
    except GardenError as p:
        print(f"Caught GardenError: {p}")
    try:
        check_water()
    except GardenError as w:
        print(f"Caught GardenError: {w}")
    print("")
    print("All custom error types work correctly!")


if __name__ == "__main__":
    main()
