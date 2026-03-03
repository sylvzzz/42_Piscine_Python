class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int,
                 color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        print(f'{self.name} (Flower): {self.height}cm, {self.age} days, '
              f'{self.color} color')
        self.bloom()

    def bloom(self) -> None:
        print(f'{self.name} is blooming beautifully!')


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: int) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        print(f'{self.name} (Tree): {self.height}cm, {self.age} days, '
              f'{self.trunk_diameter}cm diameter')
        self.produce_shade()

    def produce_shade(self) -> None:
        shade_area = (self.height * self.trunk_diameter * 3.14) / 1000
        print(f'{self.name} provides {shade_area:.0f} square meters of shade')


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str, nutritional_value: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value
        print(f'{self.name} (Vegetable): {self.height}cm, {self.age} days, '
              f'{self.harvest_season} harvest')
        self.bloom()

    def bloom(self) -> None:
        print(f'{self.name} is rich in {self.nutritional_value}')


def main():
    print("=== Garden Plant Types ===\n")
    Flower("Rose", 25, 30, "white")
    print()
    Flower("Papoila", 10, 25, "red")
    print()
    Tree("Oak", 500, 1825, 50)
    print()
    Tree("Carvalho", 800, 2825, 90)
    print()
    Vegetable("Tomato", 40, 10, "spring", "vitamin C")
    print()
    Vegetable("Carrot", 30, 15, "summer", "fiber")
    print()


if __name__ == "__main__":
    main()
