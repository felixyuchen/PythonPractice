def display_patterns(n):
    space = " "
    for i in range(1, n + 1):
        for j in range(i, n):
            print(f"{space:>3}", end="")
        for x in range(i, 0, -1):
            print(f"{x:>3}", end="")
        print()


def main():
    valid = True
    while valid:
        user_input = input("Please enter 1-99: ")
        try:
            number_input = int(user_input)
            if number_input >= 1 and number_input < 100:
                valid = False
            else:
                print("Invalid number.Please enter again")
        except ValueError:
            print("Invalid number.Please enter again")
    display_patterns(number_input)


if __name__ == "__main__":
    main()
