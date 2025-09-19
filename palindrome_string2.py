#check palindrome string
class PalindromeString2:
    def isPalindrome(self, input_str):
        leng = len(str)
        strList = list(str)
        for i in range(leng //2):
            if strList[i] != strList[-(i + 1)]:
                return False
        return True

    def main(self):
        input = "abcbdd"
        if self.isPalindrome(input):
            print(input, " is palindrome string.")
        else:
            print(input, " is not a palindrome string.")

if __name__=="__main__":
    pal = PalindromeString2()
    pal.main()