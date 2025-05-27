class Solution:
    def is_palindrome(self, s: str) -> bool:
        str_updated = ''.join([ch for ch in s if ch.isalnum()]).lower()
        str_reversed = str_updated[::-1]
        return str_updated == str_reversed

def main():
    s = "A man, a plan, a canal: Panama"
    sol = Solution()
    print(sol.is_palindrome(s))

if __name__ == "__main__":
    main()