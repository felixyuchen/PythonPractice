# 119
from typing import List


class Solution:
    def get_row(self, rowIndex: int) -> List[int]:
        triangle = []
        for i in range(rowIndex + 1):
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
            triangle.append(row)
        return triangle[-1]


def main():
    number = 3
    sol = Solution()
    print(sol.get_row(number))


if __name__ == "__main__":
    main()
