import math


def get_player_pos() -> None:
    for j in range(2):
        if j == 0:
            print("Get a first set of coordinates")
        else:
            print()
            print("Get a second set of coordinates")
        while True:
            coordinates: str = input(
                                    "Enter new coordinates as floats "
                                    "in format 'x,y,z': "
                                    )
            list_xyz: list[str] = coordinates.split(",")
            if len(list_xyz) != 3:
                print("Invalid syntax")
                continue
            valid: bool = True
            floatxyz: list[float] = []
            for i in list_xyz:
                try:
                    floatxyz.append(float(i))
                except ValueError:
                    print(
                        f"Error on parameter '{i}' : "
                        f"could not convert string to float:'{i}'"
                        )
                    valid = False
                    break
            if not valid:
                continue
            xyz: tuple[float, float, float] = (
                                                floatxyz[0],
                                                floatxyz[1],
                                                floatxyz[2]
                                                )
            x: float = xyz[0]
            y: float = xyz[1]
            z: float = xyz[2]
            if j == 0:
                first_xyz: tuple[float, float, float] = xyz
                print(f"Got a first tuple: {xyz}")
                print(
                        f"It includes: X={x}, Y={y}, Z={z}"
                    )
                distance_to_center: float = math.sqrt(x ** 2 + y ** 2 + z ** 2)
                print(f"Distance to center: {distance_to_center:.4f}")
                break
            else:
                if first_xyz:
                    distance: float = math.sqrt(
                                                (x - first_xyz[0]) ** 2 +
                                                (y - first_xyz[1]) ** 2 +
                                                (z - first_xyz[2]) ** 2
                                                )
                    print(
                        "Distance between the 2 sets "
                        f"of coordinates: {distance:.4f}"

                    )
            break


def main() -> None:
    print("=== Game Coordinate System ===\n")
    get_player_pos()


if __name__ == "__main__":
    main()
