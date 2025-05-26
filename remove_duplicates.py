from typing import List


class Solution:
    def remove_duplicates(self, nums: List[int]) -> int | None:
        if not nums:
            return 0

        slow = 0
        for fast in range(1, len(nums)):
            if nums[slow] != nums[fast]:
                slow += 1
                nums[slow] = nums[fast]
        return slow + 1


def main():
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    sol = Solution()
    print(sol.remove_duplicates(nums))


if __name__ == "__main__":
    main()
