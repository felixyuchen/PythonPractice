class Solution:
    def my_sqrt(self, x: int) -> int:
        if x < 0:
            raise ValueError("Cannot compute square root of a negative number")
        elif x == 0:
            return 0
        result = x
        while True:
            result_x = 0.5 * (result + x / result)
            if abs(result_x - result) < 1e-10:
                return result_x
            result = result_x
def main():
    x = 25
    sol = Solution()
    print(sol.my_sqrt(x))

if __name__ == "__main__":
    main()