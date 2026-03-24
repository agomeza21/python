import sys


def create_list() -> list:
    score = []
    for i in range(1, len(sys.argv)):
        try:
            score.append(int(sys.argv[i]))
        except ValueError:
            print(f"Invalid parameter: '{sys.argv[i]}'")
    return score


def main() -> None:
    print("=== Player Score Analytics ===")
    if len(sys.argv) == 1:
        print("No scores provided.", end="")
        print(" Usage: python3 ft_score_analytics.py", end="")
        print(" <score1> <score2> ...")
        return
    score = create_list()
    if len(score) == 0:
        print("No scores provided.", end="")
        print("Usage: python3 ft_score_analytics.py", end="")
        print(" <score1> <score2> ...")
        return
    print(f"Scores processed: {score}")
    print(f"Total players: {len(score)}")
    total = sum(score)
    print(f"Total score: {total}")
    print(f"Average score: {total / len(score)}")
    max_num = max(score)
    print(f"High score: {max_num}")
    min_num = min(score)
    print(f"Low score: {min_num}")
    print(f"Score range: {max_num - min_num}")


if __name__ == "__main__":
    main()
