import numpy as np


def max_profit(input_txt: str):
    prices = np.loadtxt(input_txt)

    max_profit_val = 0
    current_max_val = prices[-1]

    buy_day = sell_day = 0
    temp_sell_day = len(prices) - 1

    for i in range(len(prices) - 1, -1, -1):
        price = prices[i]

        if price > current_max_val:
            current_max_val = price
            temp_sell_day = i

        potential_profit = current_max_val - price

        if potential_profit > max_profit_val:
            max_profit_val = potential_profit
            buy_day = i
            sell_day = temp_sell_day

    print("Max Profit:", f"${max_profit_val:.2f}")
    print("Buy on day:", buy_day + 1)
    print("Sell on day:", sell_day + 1)


if __name__ == "__main__":
    input_file = rf"C:/Users/lizar/Desktop/MMM_close.txt"
    max_profit(input_file)