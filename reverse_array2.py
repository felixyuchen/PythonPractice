# reverse an array
def reverse_array(arr):
    if not arr:
        return arr
    leng = len(arr)
    left = 0
    right = leng - 1
    while left < right:
        temp = arr[left]
        arr[left] = arr[right]
        arr[right] = temp
        left += 1
        right -= 1
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
    ]

    array = reverse_array(arr)
    for i in array:
        print(f"{i} ", end="")


if __name__ == "__main__":
    main()
