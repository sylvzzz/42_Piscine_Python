import sys


def get_inventory(args: list) -> dict:
    inventory = {}

    for arg in args:
        try:
            parts = arg.split(":")
            if len(parts) != 2:
                raise ValueError(f"Invalid format: {arg}")

            item_name = parts[0].strip()
            quantity = int(parts[1].strip())

            inventory[item_name] = quantity

        except (ValueError, IndexError) as e:
            print(f"Error parsing '{arg}': {e}")
            continue

    return inventory


def calculate_total_items(inventory: dict) -> int:
    total = 0
    for quantity in inventory.values():
        total += quantity
    return total


def get_most_common(inventory: dict) -> tuple:
    if not inventory:
        return None, 0

    max_item = None
    max_qty = -1

    for item, qty in inventory.items():
        if qty > max_qty:
            max_qty = qty
            max_item = item

    return max_item, max_qty


def get_least_common(inventory: dict) -> tuple:
    if not inventory:
        return None, 0

    items = list(inventory.items())
    min_item, min_qty = items[0]

    for item, qty in inventory.items():
        if qty < min_qty:
            min_qty = qty
            min_item = item

    return min_item, min_qty


def categorize_inventory(inventory: dict) -> dict:
    categories = {
        "Moderate": {},
        "Scarce": {}
    }

    for item_name, quantity in inventory.items():
        if quantity > 4:
            categories["Moderate"][item_name] = quantity
        else:
            categories["Scarce"][item_name] = quantity

    return categories


def get_restock_suggestions(inventory: dict) -> list:
    return [item for item, qty in inventory.items() if qty <= 1]


def inventory_report(inventory: dict) -> None:
    if not inventory:
        print("Inventory is empty!")
        return

    print("=== Inventory System Analysis ===")

    total = calculate_total_items(inventory)
    unique = len(inventory)

    print(f"Total items in inventory: {total}")
    print(f"Unique item types: {unique}")

    print("\n=== Current Inventory ===")

    items_list = list(inventory.items())
    n = len(items_list)

    i = 0
    while i < n:
        j = 0
        while j < n - i - 1:
            if items_list[j][1] < items_list[j + 1][1]:
                temp = items_list[j]
                items_list[j] = items_list[j + 1]
                items_list[j + 1] = temp
            j += 1
        i += 1

    for item_name, quantity in items_list:
        percentage = (quantity / total) * 100
        unit_word = "unit" if quantity == 1 else "units"
        print(f"{item_name}: {quantity} {unit_word} ({percentage:.1f}%)")

    print("\n=== Inventory Statistics ===")
    most_item, most_qty = get_most_common(inventory)
    least_item, least_qty = get_least_common(inventory)

    print(f"Most abundant: {most_item} "
          f"({most_qty} unit{'s' if most_qty != 1 else ''})")

    print(f"Least abundant: {least_item} "
          f"({least_qty} unit{'s' if least_qty != 1 else ''})")

    print("\n=== Item Categories ===")
    categories = categorize_inventory(inventory)

    for category, items in categories.items():
        print(f"{category}: {items}")

    print("\n=== Management Suggestions ===")
    restock = get_restock_suggestions(inventory)
    print(f"Restock needed: {restock}")

    print("\n=== Dictionary Properties Demo ===")
    print(f"Dictionary keys: {list(inventory.keys())}")
    print(f"Dictionary values: {list(inventory.values())}")

    sample_item = "sword"
    sample_exists = inventory.get(sample_item) is not None
    print(f"Sample lookup - '{sample_item}' in inventory: "
          f"{sample_exists}")

    new_shipment = {"relic": 1, "gold_dust": 10}
    inventory.update(new_shipment)


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python3 ft_inventory_system.py item:qty "
              "item:qty ...")
        print("Example: python3 ft_inventory_system.py sword:1 "
              "potion:5 shield:2 armor:3 helmet:1")
        return

    inventory = get_inventory(sys.argv[1:])

    if not inventory:
        print("No valid items parsed from arguments.")
        return

    inventory_report(inventory)


if __name__ == "__main__":
    main()
