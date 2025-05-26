class Solution:
    def str_str(self, haystack: str, needle: str) -> int | None:
        h,n = len(haystack),len(needle)
        for i in range(h-n+1):
            if haystack[i:i+n] == needle:
                return i
        return -1

def main():
    haystack = "sadbutsad"
    needle = "sad"
    sol = Solution()
    print(sol.str_str(haystack,needle))

if __name__ == "__main__":
    main()