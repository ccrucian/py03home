import sys


class InvalidParameter(Exception):
    pass


def display_scores(args: list[str]) -> None:
    scores: list[int] = []
    for arg in args[1:]:
        try:
            scores.append(int(arg))
        except Exception:
            print(f"Invalid parameter: '{arg}'")
    if scores:
        print(
            f"Scores processed: {scores}\n"
            f"Total players: {(length := (len(scores)))}\n"
            f"Total score: {(somma := sum(scores))}\n"
            f"Average score: {somma / length:.1f}\n"
            f"High score: {(max_ := max(scores))}\n"
            f"Low score: {(min_ := min(scores))}\n"
            f"Score range: {max_ - min_}"
        )
    else:
        print(
            "No scores provided. Usage:python3 "
            "ft_score_analytics.py <score1> "
            "<score2> ..."
            )


def main() -> None:
    print("=== Player Score Analytics ===")
    print()
    display_scores(sys.argv)


if __name__ == "__main__":
    main()