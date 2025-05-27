from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # now[j] = now[i-1,j-1] + now[i-1,j]
        triangle = []
        for i in range(numRows):
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
            triangle.append(row)
        return triangle


def main():
    numbers = 5
    sol = Solution()
    print(sol.generate(numbers))


if __name__ == "__main__":
    main()
