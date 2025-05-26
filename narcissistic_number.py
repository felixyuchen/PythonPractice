def narc_number(n) -> bool:
    # 将正整数转成字符串，字符串的长度也就是该正整数的位数
    length = len(str(n))
    result = 0
    for i in range(length):
        # 将正整数转成字符串，获取这个字符串的一位，再转成整数，**是幂的意思
        result += int(str(n)[i]) ** length
    return result == n


def main():
    number_list = []
    for i in range(100, 100000):
        if narc_number(i):
            #将满足条件的水仙花数放入一个列表number_list中，以便后续对其操作，比如按某种格式输出
            number_list.append(i)
            # join不能拼接数字，只能拼接字符串，如果number_list里面都是字符串，用join拼接可以直接写成 ",".join(number_list)，其中join之前的逗号是分割符号
    print("Narcissistic number is:",",".join(str(n) for n in number_list))


if __name__ == "__main__":
    main()
