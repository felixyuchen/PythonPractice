def sumDigits(n):
    sum = 0
    iniInteger = 234
    while iniInteger > 0:
        sum += int(iniInteger % 10)
        iniInteger = iniInteger / 10
    return sum

def main():
    print(sumDigits(234))
    
if __name__ == "__main__":
    main()

