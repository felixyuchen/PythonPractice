#返回一个长度为 n 的斐波那契数列。
def fib(n) -> list:
    first, second = 0, 1
    my_list = [first, second]
    for _ in range(n - 2):
        first, second = second, first + second
        my_list.append(second)
    return my_list


def main():
    try:
        user_input = int(input("Please enter a number: "))
        if user_input < 0:
            print("Please enter greater 0 number")
            return
        result = fib(user_input)
        print(f"Before {user_input} numbers: {result}")
    except ValueError:
        print("The number invalid.")


if __name__ == "__main__":
    main()
