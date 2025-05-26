def fac(number):
    result = 1
    for i in range(2, number + 1):
        result *= i
    return result


def main():
    number = 5
    print(fac(number))


if __name__ == "__main__":
    main()
