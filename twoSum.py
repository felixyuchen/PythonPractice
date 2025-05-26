from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hashmap:
                return [hashmap[complement], i]
            hashmap[num] = i


def main():
        nums = [2, 7, 11, 15]
        target = 9
        solution = Solution()
        print(solution.twoSum(nums, target))


if __name__ == "__main__":
        main()
