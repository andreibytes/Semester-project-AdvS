import numpy as np


def compute_stats(input_txt: str):
    data = np.loadtxt(input_txt)

    with open(input_txt, "r") as f:
        first_line = f.readline().strip()

    if "." in first_line:
        decimals = len(first_line.split(".")[1])
    else:
        decimals = 0

    # One more decimal place
    out_decimals = decimals + 1
    fmt = f"%.{out_decimals}f"


    # Compute statistics
    mean_val = np.mean(data)
    std_val = np.std(data)

    print("Mean:", fmt % mean_val)
    print("Standard Deviation:", fmt % std_val)



if __name__ == "__main__":
    input_file = rf"C:/Users/lizar/Desktop/MMM_close.txt"
    compute_stats(input_file)