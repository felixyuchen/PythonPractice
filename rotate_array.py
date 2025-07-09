#189
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        nums[:] = nums[-k:] + nums[:-k]

def main():
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    sol = Solution()
    sol.rotate(nums,k)
    print(nums)

if __name__ == "__main__":
    main()
