#打印出只出现一次的字符串
from collections import Counter
def different_number(arr):
    return Counter(arr)


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
    count = different_number(arr)
    print(count)
    for key, value in count.items():
        if value == 1:
            print(f"{key} ")


if __name__ == "__main__":
    main()
