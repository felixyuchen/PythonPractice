class Solution:
    def isValid(self, s: str) -> bool:
        if s[0] == ")" or s[0] == "}" or s[0] == "]":
            return False
        stack = []
        for i in s:
            if i == "(" or i == "{" or i == "[":
                stack.append(i)
            elif i == ")" and stack and stack[-1] == "(":
                stack.pop()
            elif i == "}" and stack and stack[-1] == "{":
                stack.pop()
            elif i == "]" and stack and stack[-1] == "[":
                stack.pop()
            else:
                return False
        return not stack


def main():
    s = "({[{}]})"
    sol = Solution()
    print(sol.isValid(s))


if __name__ == "__main__":
    main()
