class GardenManager:
    def __init__(self, name):
        self.name = name
        self.plants = []

    def add_plant(self, plant):
        self.plants.append(plant)

    def remove_plant(self, plant):
        if plant in self.plants:
            self.plants.remove(plant)

    def get_all_plants(self):
        return self.plants
