import numpy as np
import matplotlib.pyplot as plt


def plot_closing_prices(input_txt: str, ticker: str):
    # Load data
    prices = np.loadtxt(input_txt)

    # X-axis: 1 to N
    days = np.arange(1, len(prices) + 1)

    # Plot
    plt.plot(days, prices)
    plt.title(f"{ticker} Closing Price")
    plt.xlabel("Day")
    plt.ylabel("Closing Price")

    plt.grid()
    plt.show()


if __name__ == "__main__":
    input_file = rf"C:/Users/lizar/Desktop/MMM_close.txt"
    plot_closing_prices(input_file, ticker="MMM")