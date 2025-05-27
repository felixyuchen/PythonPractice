class Solution:
    def climb_stairs(self, n: int) -> int:
        if n <= 2:
            return n
        dp = [0] * (n+1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[n]

def main():
    n = 3
    sol = Solution()
    print(sol.climb_stairs(n))

if __name__ == "__main__":
    main()