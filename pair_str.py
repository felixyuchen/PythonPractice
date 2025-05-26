from itertools import combinations


def main():
    arr = [
        "computer",
        1,
        2,
        2,
        3,
        "apple",
        "banana",
        "apple",
        "orange",
    ]
    count = 0
    for pair in combinations(arr, 2):
        print(f"{pair}, ", end="")
        count += 1
        if count % 5 == 0:
            print()


if __name__ == "__main__":
    main()
