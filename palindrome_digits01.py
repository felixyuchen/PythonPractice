class Solution:
    def isPalindrome(self, x: int) -> bool:
        reserved = 0
        saved_x = x
        while x > 0:
            reserved = reserved * 10 + x % 10
            x = x // 10
        return saved_x == reserved
    
def main():
    x = 121
    solution = Solution()
    print(solution.isPalindrome(x))

if __name__ == "__main__":
    main()