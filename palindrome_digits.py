class Solution:
    def reversed_number(self, number):
        result = 0
        while number != 0:
            lastNumber = number % 10
            result = result * 10 + lastNumber
            number //= 10
        return result


    def is_palindrome(self, num):
        return num == self.reversed_number(num)


def main():
    isValid = True
    while isValid:
        user_input = input("Please enter a number: ")
        try:
            number_input = int(user_input)
            isValid = False
        except ValueError:
            print("Invalid input! Please enter a valid integer.")
    solution = Solution()
    if solution.is_palindrome(number_input): 
        print("This is a palindrome number.")
    else:
        print("This is not a palindrome number.")


if __name__ == "__main__":
    main()
