import sys


def num_args() -> None:
    if len(sys.argv) == 1:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {len(sys.argv) - 1}")


def args() -> None:
    for i in range(1, len(sys.argv)):
        print(f"Argument {i}: {sys.argv[i]}")


def main() -> None:
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")
    num_args()
    args()
    print(f"Total arguments: {len(sys.argv)}")


if __name__ == "__main__":
    main()
