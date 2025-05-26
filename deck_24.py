import random


def create_deck():
    deck = []
    for point in range(1, 14):
        deck += [point] * 4
    return deck


def count_24_groups(deck):
    count_24 = 0
    for i in range(0, len(deck), 4):
        group = deck[i : i + 4]
        total = sum(group)
        if total == 24:
            count_24 += 1
    return count_24


def main():
    deck = create_deck()
    random.shuffle(deck)
    result = count_24_groups(deck)
    print(f"{result}")


if __name__ == "__main__":
    main()
