import sys

inventory: dict[str, int] = {}


def create_inventory(args) -> dict[str, int]:
    for item in args:
        try:
            name, val = item.split(":")
            if name in inventory.keys():
                    print(f"Redundant item '{name}' - discarding")
                    continue
            if not val.isdigit():
                    print(
                            f"Quantity error for '{name}': invalid "
                            f"literal for int() with base 10 : '{val}'"
                        )
                    continue
            val = int(val)
            inventory[name] = val
        except ValueError:
            print(f"Error - invalid parameter '{item}'")
    return inventory


def sum_values(inventory: dict[str, int]) -> int:
    total: int = 0
    for value in inventory.values():
        total += value
    return total


def find_min(inv: dict(str, int)) -> tuple[str, int]:
    minus = values
    for i in values[1:]:
        if i < minus:
            minus = i
    return i
          

def main() -> None:
    print(f"=== Inventory System Analysis ===")
    inventory = create_inventory(sys.argv[1:])
    print(f"Got inventory: {inventory}")
    print(f"Item list: {[val for val in inventory.keys()]}")
    total: int = sum_values(inventory)
    print(f"Total quantity of the {len(inventory)} items: {total}")
    max: int = 0
    # min: int = 0
    for name, val in inventory.items():
        if val > max:
            max = val
            name_max: str = name
        percent: float = round(((val / total) * 100), 1)
        print(f"Item {name} represents {percent}%")
    print(f"Item most abundant: {name_max} with quantity {max}")
    values = list(inventory.values())


if __name__ == "__main__":
    main()
