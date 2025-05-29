#151

class Solution:
    def reverse_words(self, s: str) -> str:
        return ' '.join(s.split()[::-1])

def main():
    s = "  hello world  "
    sol = Solution()
    print(sol.reverse_words(s))

if __name__ == "__main__":
    main()