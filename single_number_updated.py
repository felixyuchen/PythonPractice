from typing import List


class Solution:
    def single_number(self, nums: List[int]) -> int | None:
        result = 0
        for item in nums:
            result ^= item
        return result

def main():
    nums = [4, 1, 2, 1, 2]
    sol = Solution()
    print(sol.single_number(nums))

if __name__ == "__main__":
    main()