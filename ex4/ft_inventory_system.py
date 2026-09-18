import sys

inventory: dict[str, int] = {}


def create_inventory(args: list[str]) -> dict[str, int]:
    inventory = {}
    for item in args:
        try:
            name, val = item.split(":")
            if name in inventory:
                print(f"Redundant item '{name}' - discarding")
                continue
            try:
                value = int(val)
                inventory[name] = value
            except ValueError as e:
                print(
                        f"Quantity error for '{name}':"
                        f"{e}: '{val}'"
                        )
        except ValueError:
            print(f"Error - invalid parameter '{item}'")
    return inventory


def sum_values(inventory: dict[str, int]) -> int:
    total: int = 0
    for value in inventory.values():
        total += value
    return total


def find_min(inv: dict[str, int]) -> tuple[str, int]:
    if not inv:
        return ("", 0)
    list_inv = the_items(inv)
    minus = list_inv[0][1]
    name_min = list_inv[0][0]
    for name, value in the_items(inv):
        if value < minus:
            minus = value
            name_min = name
    return (name_min, minus)


def the_items(inv: dict[str, int]) -> list[tuple[str, int]]:
    result = []
    for key in inv:
        value = inv[key]
        result.append((key, value))
    return result


def main() -> None:
    print("=== Inventory System Analysis ===")
    inventory = create_inventory(sys.argv[1:])
    print(f"Got inventory: {inventory}")
    print(f"Item list: {inventory.keys()}")
    total: int = sum_values(inventory)
    print(f"Total quantity of the {len(inventory)} items: {total}")
    max: int = 0
    name_max: str = ""
    for name, val in the_items(inventory):
        if val > max:
            max = val
            name_max = name
        percent: float = round(((val / total) * 100), 1)
        print(f"Item {name} represents {percent}%")
    print(f"Item most abundant: {name_max} with quantity {max}")
    least_ = find_min(inventory)
    print(
        f"Item least abundant: {least_[0]}"
        f"with quantity {least_[1]}"
        )
    inventory.update(pere=10)
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
