#001 返回list里面两个数的和等于target的list下标
from typing import List, Any


class Solution:
    def two_sum(self, nums: List[int], target: int) -> list[int | Any] | None:
        hashmap = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hashmap:
                return [hashmap[complement], i]
            hashmap[num] = i
        return None


def main():
        nums = [2, 7, 11, 15]
        target = 9
        solution = Solution()
        print(solution.two_sum(nums, target))


if __name__ == "__main__":
        main()
