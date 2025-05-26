def reverse(arr):
    length = len(arr)
    for i in range(length // 2):
        temp = arr[i]
        arr[i] = arr[length - i - 1]
        arr[length - i - 1] = temp
    return arr


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
        "banana",
        "banana",
    ]
    reversed_arr = arr[::-1]
    for i in reversed_arr:
        print(f"{i} ", end="")
    print()
    array = reverse(arr)
    for i in array:
        print(f"{i} ", end="")


if __name__ == "__main__":
    main()
