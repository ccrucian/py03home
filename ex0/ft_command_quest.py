import sys


def print_args(args: list[str]) -> None:
    print(f"Program name: {args[0]}")
    number: int = len(args)
    if number > 1:
        print(f"Arguments received: {number}")
        for i in range(1, number):
            print(f"Argument {i}: {args[i]}")
    else:
        print("No arguments provided!")
    print(f"Total arguments: {number}")


def main() -> None:
    print("=== Command quest ===")
    print_args(sys.argv)


if __name__ == "__main__":
    main()
