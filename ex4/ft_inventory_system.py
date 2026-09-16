import sys


class QuantityError(Exception):
    pass

class RedundantError(Exception):
    pass

inventory: dict[str, int] = {}

def create_inventory(args) -> dict[str, int]:
    for item in args:
        try:
            name, val = item.split(":")
            if name in inventory.keys():  
                inventory[name] = val
            raise RedundantError:
                print(f"Redundant item {name}")
        except ValueError:
            print(f"Error - invalid parameter '{item}'")
    return inventory
            



def main() -> None:
    inventory = create_inventory(sys.argv[1:])
    print(f"{inventory}")


if __name__ == "__main__":
    main()