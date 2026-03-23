import sys


def create_list() -> list:
    score = []
    for i in range(1, len(sys.argv)):
        score.append(sys.argv[i])
    return score


def main() -> None:
    print("=== Player Score Analytics ===")
    score = create_list()
    print(f"Scores processed: {score}")


if __name__ == "__main__":
    main()
