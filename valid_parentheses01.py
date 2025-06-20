class Solution:
    def is_valid(self, s: str) -> bool:
        stack = []
        mapping = {'(':')','[':']','{':'}'}
        for ch in s:
            if ch in mapping:
                stack.append(ch)
            elif ch in mapping.values():
                if not stack or mapping[stack[-1]] != ch:
                    return False
                stack.pop()
            else:
                return False
        return not stack

def main():
    s = "({[{}]})"
    sol = Solution()
    print(sol.is_valid(s))


if __name__ == "__main__":
    main()