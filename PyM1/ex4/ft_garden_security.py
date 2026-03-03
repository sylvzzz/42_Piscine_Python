class SecurePlant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self._name = name
        self._height = height
        self._age = age

    def set_height(self, height: int) -> None:
        if (height < 0):
            print()
            print(f"Invalid opeation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected\n")
        else:
            self._height = height
            print(f"Height updated: {self.get_height()} [OK]")

    def set_age(self, age: int) -> None:
        if (age < 0):
            print(f"Invalid opeation attempted: age {age}days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self._age = age
            print(f"Age updated: {self.get_age()} [OK]")

    def get_height(self) -> int:
        return self._height

    def get_age(self) -> int:
        return self._age


def main():
    rose = SecurePlant("Rose", 25, 30)

    print("=== Garden Security System ===")
    print(f"Plant created: {rose._name}")
    rose.set_age(50)
    rose.set_height(75)
    height = rose.get_height()
    age = rose.get_age()
    rose.set_height(-5)
    print(f"Current plant: {rose._name} ({height}cm, {age}days)")


if __name__ == "__main__":
    main()
