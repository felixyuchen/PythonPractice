

from typing import List


class Solution:
    def majority_element(self, nums: List[int]) -> int | None:
        counter={}
        size = len(nums)
        for num in nums:
            if num in counter:
                counter[num] +=1
            else:
                counter[num] = 1

        for key, value in counter.items():
            if value > size // 2:
                return key
        return None

def main():
    nums = [2, 2, 1, 1, 1, 2, 2]
    sol = Solution()
    print(sol.majority_element(nums))

if __name__ == "__main__":
    main()
