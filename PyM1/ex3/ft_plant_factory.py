class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 5, 90)
    fern = Plant("Fern", 15, 120)
    oak = Plant("Oak", 200, 365)
    plants = [rose, sunflower, oak, cactus, fern]
    print("=== Plant Factory Output ===")
    for i in range(len(plants)):
        print(f"{plants[i].name}: {plants[i].height}cm, {plants[i].age} days old")
    print()
    print(f"Total plants created: {i+1}")