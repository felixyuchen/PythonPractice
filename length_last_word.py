class Solution:
    def length_last_word(self, s: str) -> int:
        parts = s.strip().split()
        return len(parts[-1])

def main():
    s = "   fly me   to   the moon  "
    sol = Solution()
    print(sol.length_last_word(s))

if __name__ == "__main__":
    main()