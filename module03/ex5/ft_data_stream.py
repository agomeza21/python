from typing import Generator
import random


def gen_event(players: list, actions: list) -> Generator:
    while True:
        name = random.choice(players)
        action = random.choice(actions)
        event = (name, action)
        yield event


def consume_event(event_list: list) -> Generator:
    while len(event_list) > 0:
        element = random.choice(event_list)
        event_list.remove(element)
        yield element


if __name__ == "__main__":
    players = ["alice", "bob", "charlie", "dylan"]
    actions = ["run", "eat", "sleep", "grab", "move",
               "climb", "swim", "release", "use", "jump"]
    gen = gen_event(players, actions)
    for i in range(1000):
        event = next(gen)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")
    event_list = []
    for i in range(10):
        add_to_list = next(gen)
        event_list.append(add_to_list)
    print(f"Built list of 10 events: {event_list}")
    for element in consume_event(event_list):
        print(f"Got event from list: {element}")
        print(f"Remains in list: {event_list}")
