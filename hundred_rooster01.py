def main():
    for rooster in range(21):
        for hen in range(34):
            chicken = 100 - rooster - hen
            if chicken % 3 == 0:
                if rooster * 5 + hen * 3 + chicken // 3 == 100:
                    print(f"Rooster:{rooster}, Hen:{hen}, Chicken:{chicken}")


if __name__ == "__main__":
    main()