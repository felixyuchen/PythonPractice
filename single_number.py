from typing import List


class Solution:
    def single_number(self, nums: List[int]) -> int:
        counter = dict()
        for key in nums:
            counter[key] = counter.get(key,0) + 1
        for key, value in counter.items():
            if value == 1:
                return key
        return 0

def main():
    nums = [4, 1, 2, 1, 2]
    sol = Solution()
    print(sol.single_number(nums))

if __name__ == "__main__":
    main()
