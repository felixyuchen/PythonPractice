def main():
    # for rooster in range(21):
    #     for hen in range(34):
    #         chicken = 100 - rooster - hen
    #         if chicken % 3 == 0:
    #             if rooster * 5 + hen * 3 + chicken // 3 == 100:
    #                 print(f"Rooster:{rooster}, Hen:{hen}, Chicken:{chicken}")

    #使用以下的代数公式去掉一层循环
    # 5r + 3h + (100 - r - h)/3 == 100
    # => 15r + 9h + (100 - r - h) == 300    # 两边乘以3
    # => 15r + 9h + 100 - r - h == 300
    # => 14r + 8h == 200
    for rooster in range(21):
        remainder  = 200 - 14 * rooster
        if remainder % 8 == 0:
            hen = remainder // 8
            chicken = 100 - rooster - hen
            if hen >= 0 and chicken >= 0 and chicken % 3 == 0:
                print(f"Rooster:{rooster}, Hen:{hen}, Chicken:{chicken}")



if __name__ == "__main__":
    main()