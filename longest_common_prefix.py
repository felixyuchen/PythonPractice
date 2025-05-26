class Solution:
    def longestCommonPrefix(self, str1, str2) -> str:
        min_len = min(len(str1), len(str2))
        str_prefix = ""
        for i in range(min_len):
            if str1[i] == str2[i]:
                str_prefix += str1[i]
            else:
                break
        return str_prefix

    def common_prefix_list(self, strs: list[str]) -> str:
        if not strs:
            return ""
        str_prefix = strs[0]
        for i in range(len(strs)):
            str_prefix = self.longestCommonPrefix(str_prefix, strs[i])
        return str_prefix


def main():
    sol = Solution()
    strs = ["cir", "car"]
    print(sol.common_prefix_list(strs))


if __name__ == "__main__":
    main()
