import heapq


def main():
    list1 = [1, 3, 6, 7]
    list2 = [2, 4, 6, 8]

    merged = list(heapq.merge(list1, list2))
    print(merged)


if __name__ == "__main__":
    main()
