#67
#给定2个二进制字符串，将其相加成为一个二进制字符串
class Solution:
    def add_binary(self, a: str, b: str) -> str:
        # return bin(int(bin(int(a))[2:])+int(bin(int(b))[2:]))[2:]
        result = []
        carry = 0
        i, j = len(a) - 1, len(b) - 1
        while i >= 0 or j >= 0 or carry:
            bit_a = int(a[i]) if i >= 0 else 0
            bit_b = int(b[j]) if j >= 0 else 0
            total = bit_a + bit_b + carry
            result.append(str(total % 2))
            carry = total // 2
            i -= 1
            j -= 1

        return "".join(reversed(result))


def main():
    a = '11'
    b = '1'
    sol = Solution()
    print(sol.add_binary(a, b))


if __name__ == "__main__":
    main()
