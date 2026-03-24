import sys


def parse_inventory() -> dict:
    inventory = {}
    for i in range(1, len(sys.argv)):
        parts = sys.argv[i].split(":")
        if len(parts) != 2:
            print(f"Error - invalid parameter '{sys.argv[i]}'")
            continue
        if parts[0] in inventory:
            print(f"Redundant item '{parts[0]}' - discarding")
            continue
        try:
            inventory[parts[0]] = int(parts[1])
        except ValueError as v:
            print(f"Quantity error for '{parts[0]}': {v}")
            continue
    return inventory


def main() -> None:
    print("=== Inventory System Analysis ===")
    inventory = parse_inventory()
    print(f"Got inventory: {inventory}")
    inventory_list = []
    for key in inventory.keys():
        inventory_list.append(key)
    print(f"Item list: {inventory_list}")
    total = 0
    for value in inventory.values():
        total = total + value
    print(f"Total quantity of the {len(inventory_list)} items: {total}")
    for key, value in inventory.items():
        percent = value / total * 100
        print(f"Item {key} represents {percent:.1f}%")
    max_num = float('-inf')
    max_item = ""
    for key, value in inventory.items():
        if value > max_num:
            max_num = value
            max_item = key
    print(f"Item most abundant: {max_item} with quantity {max_num}")
    min_num = float('inf')
    min_item = ""
    for key, value in inventory.items():
        if value < min_num:
            min_num = value
            min_item = key
    print(f"Item least abundant: {min_item} with quantity {min_num}")
    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
