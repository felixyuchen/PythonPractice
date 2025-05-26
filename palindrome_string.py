class PalindromeString:
    def is_palindrome(self, str):
        chars = list(str)
        length = len(chars)
        for i in range(length // 2):
            if chars[i] != chars[-(i + 1)]:
                return False
        return True

    def main(self):
        user_input = input("Please enter a string: ")
        if self.is_palindrome(user_input):
            print(user_input, "is the palindrome.")
        else:
            print(user_input, "is not the palindrome.")


if __name__ == "__main__":
    pal = PalindromeString()
    pal.main()
