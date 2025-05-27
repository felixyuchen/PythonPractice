
from typing import List


class Solution:
    def plus_one(self, digits: List[int]) -> List[int]:
        if not all(0 <= d <= 9 for d in digits):
            print("Error: digits must all be in the range 0 to 9.")
            return []
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += 1
            if digits[i] != 10:
                return digits
            else:
                digits[i] = 0
        if digits[0] == 0:
            digits.insert(0, 1)
        return digits


def main():
    digits = [7, 0, 9, 9]
    sol = Solution()
    print(sol.plus_one(digits))


if __name__ == "__main__":
    main()
