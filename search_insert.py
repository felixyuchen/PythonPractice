from typing import List


class Solution:
    def search_insert(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] > target:
                high = mid - 1
            elif nums[mid] == target:
                return mid
            else:
                low = mid + 1
        return low


def main():
    nums = [1, 3, 5, 6]
    target = 5
    sol = Solution()
    print(sol.search_insert(nums, target))


if __name__ == "__main__":
    main()
