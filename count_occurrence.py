from collections import Counter


def count_occurrence(arr):
    counter = Counter(arr)
    return counter


def main():
    arr = [1, 2, 2, 3, "apple", "banana", "apple", "orange", "banana", "banana"]
    count = count_occurrence(arr)
    print(count)
    for key, value in count.items():
        print(f"{key}:{value}")


if __name__ == "__main__":
    main()
