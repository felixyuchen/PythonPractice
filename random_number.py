from collections import Counter
import random


def random_number():
    arr = []
    for i in range(0,100):
        arr.append(random.randint(0, 9))
    count = Counter(arr)
    return count


def main():
    count = random_number()
    for key in sorted(count):
        print(f"{key}:{count[key]}, ", end="")


if __name__ == "__main__":
    main()
