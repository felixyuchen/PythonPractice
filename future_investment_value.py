def future_investment_value(investment_amount, interest_rate, years):
    monthly_interest_rate = interest_rate * 0.01
    # future_investment_value=0
    rate_value = 1
    for i in range(1, years * 12 + 1):
        rate_value *= 1 + monthly_interest_rate / 12
    return investment_amount * float(rate_value)


def main():
    print(round(future_investment_value(1000.56, 4.25, 1), 2))


if __name__ == "__main__":
    main()
