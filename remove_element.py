from typing import List


class Solution:
    def remove_element(self, nums: List[int], val: int) -> int | None:
        left = 0
        for right in range(len(nums)):
            if nums[right] != val:
                nums[left] = nums[right]
                left += 1
        return left


def main():
    nums = [3, 2, 2, 3]
    val = 3
    sol = Solution()
    print(sol.remove_element(nums, val))


if __name__ == "__main__":
    main()
