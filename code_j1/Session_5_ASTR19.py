#session 5 prompt ASTR_19

import math

#Write a Python program that writes out a table of the function sin(x) vs. x,
#where x is tabulated between 0 and 2 with a thousand entries.
#Follow the basic Python program structure,
#including a main program function.

def generate_sin_table():
    table = []
    for i in range(1001):
        x = i / 500.0
        sin_x = math.sin(x)
        table.append((sin_x, x))
    return table

def main():
    sin_table = generate_sin_table()

    # Print the table header
    print("sin(x)\t\t x")
    print("-----------------------")

    # Print the table content
    for x, sin_x in sin_table:
        print(f"{x:.4f}\t\t {sin_x:.3f}")

if __name__ == "__main__":
    main()
