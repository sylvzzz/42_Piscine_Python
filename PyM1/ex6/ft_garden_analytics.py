class Plant:
    def __init__(self, name: str, initial_height: int) -> None:
        self.name = name
        self.set_height(initial_height)

    def set_height(self, new_height: int) -> None:
        if (new_height < 0):
            self.height = 0
        else:
            self.height = new_height

    def get_height(self) -> int:
        return self.height

    def details(self) -> str:
        return f"{self.name}: {self.height}cm"

    def grow(self) -> None:
        self.height += 1
        print(f"{self.name} grew 1cm")

    def get_category(self) -> str:
        return "regular"


class FloweringPlant(Plant):
    def __init__(self, name: str, initial_height: int, color: str) -> None:
        super().__init__(name, initial_height)
        self.color = color

    def details(self) -> str:
        base_details = super().details()
        return f"{base_details}, {self.color} flowers (blooming)"

    def get_category(self) -> str:
        return "flowering"


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, color, prize_points):
        super().__init__(name, height, color)
        self.prize_points = prize_points

    def details(self):
        return (f'{self.name}: {self.height}cm, {self.color} '
                f'flowers (blooming), Prize points: {self.prize_points}')

    def get_category(self) -> str:
        return "prize"


class Garden:
    def __init__(self, owner: str) -> None:
        self.owner = owner.title()
        self.plants = []
        self.total_growth = 0

    def add_plant(self, plant: Plant) -> None:
        self.plants.append(plant)
        plant.name = plant.name.title()
        print(f"Added {plant.name} to {self.owner}'s garden")

    def help_grow(self) -> None:
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()
            self.total_growth += 1

    def get_stats(self) -> tuple[int, int]:
        return len(self.plants), self.total_growth

    def report(self) -> None:
        print(f"=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            print(f"- {plant.details()}")


class GardenManager:
    total_gardens = 0

    class GardenStats:
        def calculate_score(self, plants: list[Plant]) -> tuple[int, ...]:
            total_score = 0
            total_regular = 0
            total_flowering = 0
            total_prize = 0

            for plant in plants:
                total_score += plant.get_height()

                category = plant.get_category()

                if category == "prize":
                    total_prize += 1
                elif category == "flowering":
                    total_flowering += 1
                else:
                    total_regular += 1

            return total_score, total_regular, total_flowering, total_prize

    def __init__(self) -> None:
        self.gardens = []
        self.stats = self.GardenStats()

    def add_garden(self, garden: Garden) -> None:
        self.gardens.append(garden)
        GardenManager.total_gardens += 1

    @staticmethod
    def height_validation(value: int) -> bool:
        if value >= 0:
            return True
        return False

    @classmethod
    def create_system(cls) -> "GardenManager":
        print("=== Garden Manager System Demo ===\n")
        return cls()


def main():
    AliceGarden = Garden("Alice")
    BobGarden = Garden("Bob")
    manager = GardenManager.create_system()
    Oak = Plant("Oak Tree", 250)
    Rose = FloweringPlant("Rose", 26, "red")
    Sunflower = PrizeFlower("Sunflower", 71, "yellow", 12)
    Tulip = Plant("Sunflower", 92)
    manager.add_garden(AliceGarden)
    manager.add_garden(BobGarden)
    AliceGarden.add_plant(Oak)
    AliceGarden.add_plant(Rose)
    AliceGarden.add_plant(Sunflower)
    BobGarden.add_plant(Tulip)
    print()
    AliceGarden.help_grow()
    print()
    AliceGarden.report()
    print()
    score_A, regular, flowering, prize_flowers = manager.stats.calculate_score(
        AliceGarden.plants)
    AlicePlants = AliceGarden.get_stats()
    print(f"Plants added: {AlicePlants[0]}, Total growth: {AlicePlants[1]}cm")
    print(f'Plant types: {regular} regular, {flowering} flowering, '
          f'{prize_flowers} prize flowers')
    print()
    print(f"Height validation test: {manager.height_validation(Oak.height)}")
    score_B = manager.stats.calculate_score(BobGarden.plants)
    print(f'Garden scores - {AliceGarden.owner}: {score_A},'
          f' {BobGarden.owner}: {score_B[0]}')
    print(f"Total gardens managed: {manager.total_gardens}")


if __name__ == "__main__":
    main()
