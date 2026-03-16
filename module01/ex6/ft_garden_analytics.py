class Plant:
    def __init__(self, name: str, height: int) -> None:
        self.name = name
        self.height = height

    def grow(self) -> int:
        unit = 1
        self.height += unit
        return unit


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, color: str) -> None:
        super().__init__(name, height)
        self.color = color

    @staticmethod
    def bloom() -> str:
        return "(blooming)"


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, color: str,
                 prize: int) -> None:
        super().__init__(name, height, color)
        self.prize = prize


class GardenManager:
    total_gardens = 0

    def __init__(self, p_name: str) -> None:
        GardenManager.total_gardens += 1
        self.p_name = p_name
        self.plants: list[Plant] = []
        self.growth = 0

    def add_plants(self, plant: Plant) -> None:
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.p_name}'s garden")

    def plant_growth(self) -> None:
        print(f"{self.p_name} is helping all plants grow...")
        for plant in self.plants:
            self.growth = plant.grow()
            print(f"{plant.name} grew {self.growth}cm")

    def report(self) -> None:
        print("Plants in garden:")
        for plant in self.plants:
            if isinstance(plant, PrizeFlower):
                print(f"- {plant.name}: {plant.height}cm,"
                      f" {plant.color} flowers {plant.bloom()},"
                      f" Prize points: {plant.prize}")
            elif isinstance(plant, FloweringPlant):
                print(f"- {plant.name}: {plant.height}cm,"
                      f" {plant.color} flowers {plant.bloom()}")
            else:
                print(f"- {plant.name}: {plant.height}cm")
        stats = GardenManager.GardenStats(self.plants, self.growth)
        print("")
        print(f"Plants added: {stats.total_plants}, Total growth: "
              f"{stats.total_growth}cm")
        print(f"Plant types: {stats.count_plant} regular, "
              f"{stats.count_flowering} flowering, {stats.count_prize} "
              "prize flowers")

    def is_valid_height(self) -> bool:
        for plant in self.plants:
            if plant.height < 0:
                return False
        return True

    @classmethod
    def create_garden_network(cls) -> None:
        print(f"Total gardens managed: {cls.total_gardens}")

    def garden_score(self) -> int:
        scores = 0
        for plant in self.plants:
            scores = scores + plant.height
            if isinstance(plant, PrizeFlower):
                scores = scores + plant.prize
        return scores

    class GardenStats:
        def __init__(self, plants: list[Plant], growth: int) -> None:
            self.total_plants = len(plants)
            self.count_prize = 0
            self.count_flowering = 0
            self.count_plant = 0
            for plant in plants:
                if isinstance(plant, PrizeFlower):
                    self.count_prize += 1
                elif isinstance(plant, FloweringPlant):
                    self.count_flowering += 1
                else:
                    self.count_plant += 1
            self.total_growth = growth * self.total_plants


def main() -> None:
    gardens = [
        GardenManager("Alice"),
        GardenManager("Bob")
    ]
    plants = [
        Plant("Oak Tree", 100),
        FloweringPlant("Rose", 25, "red"),
        PrizeFlower("Sunflower", 50, "yellow", 10)
    ]
    plant_bob = Plant("Pine Tree", 90)
    print("=== Garden Management System Demo ===")
    print("")
    for plant in plants:
        gardens[0].add_plants(plant)
    gardens[1].add_plants(plant_bob)
    print("")
    gardens[0].plant_growth()
    print("")
    print(f"=== {gardens[0].p_name}'s Garden Report ===")
    gardens[0].report()
    print("")
    print(f"Height validation test: {gardens[0].is_valid_height()}")
    print(f"Garden scores - {gardens[0].p_name}: {gardens[0].garden_score()},"
          f" {gardens[1].p_name}: {gardens[1].garden_score()}")
    gardens[0].create_garden_network()


if __name__ == "__main__":
    main()
