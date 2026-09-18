import typing
import random


players: list[str] = [
                    "Alice", "Flami", "Betta",
                    "Francesca", "Lilla", "Fra",
                    "Carli"
                    ]


actions: list[str] = [
    "is writing a message", "is calling Matteo",
    "is at work", "is on a call",
    "got drunk", "took a poop",
    "is at a wedding", "is anxious",
    "is in Circeo", "is in Punta Ala",
    "is humming", "is at the therapist",
    "is driving", "setting up the GPS",
    "is getting married", "is going to the gym",
    "has skept the gym", "flaked out",
    "booking a restaurant", "is smoking weed",
    "wants to go on a trip",
    "is going to Puglia", "is no longer on Hinge",
    "is going to Brunico", "being a bitch",
    "is going down to the garden",
    "won at Monopoly", "sleeps",
    "is arguing over Monopoly", "is Carli",
    "will win Fantasanremo", "screams Francesco",
    "is winning the 2027 poop contest",
    "is watching the birds", "will get a partner",
    "is logorroic", "is spettagolando"
                    ]


def gen_events(
        players: list[str], actions: list[str]
        ) -> typing.Iterator[tuple[str, str]]:
    while True:
        player = random.choice(players)
        action = random.choice(actions)
        yield (player, action)


def consume_events(
        ten_events: list[tuple[str, str]]
        ) -> typing.Iterator[list[tuple[str, str]]]:
    while ten_events:
        removed = random.choice(ten_events)
        ten_events.remove(removed)
        print(f"Got event from list: {removed}")
        yield ten_events


def main() -> None:
    for i in range(1, 1001):
        event = next(gen_events(players, actions))
        print(f"Event {i}: {event[0]} {event[1]}")
    ten_events = []
    for i in range(10):
        ten_events.append(next(gen_events(players, actions)))
    print(f"Built list of 10 events: {ten_events}")
    removed = consume_events(ten_events)
    while ten_events:
        next(removed)
        print(f"Remains in list: {ten_events}")


if __name__ == "__main__":
    main()
