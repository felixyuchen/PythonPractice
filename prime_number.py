import math


def is_prime(number):
    flag = True
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            flag = False
            break
    return flag


def main():
    number = 20
    if is_prime(number):
        print("The number ", number, " is a prime.")
    else:
        print("The number ", number, " is not a prime.")


if __name__ == "__main__":
    main()
