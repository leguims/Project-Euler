Enonce = """
Champernowne's constant

Problem 40
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 x d10 x d100 x d1000 x d10000 x d100000 x d1000000
"""

import EulerTools
import time

def main():
    print(40*"=")
    print(Enonce)
    print(40*"-")
    
    maxi_index = 1_000_000
    d="."
    start = time.perf_counter()
    for i in range(1, maxi_index):
        d += str(i)
        if len(d) > maxi_index:
            break
    #print(d)
    factors = list()
    for i in [1, 10, 100, 1_000, 10_000, 100_000, 1_000_000]:
        #print(f"i={i}")
        factors.append(int(d[i]))
        #print(f"factors={factors}")
    print(f"factors={factors}")
    Solution = int(d[1]) * int(d[10]) * int(d[100]) * int(d[1_000]) * int(d[10_000]) * int(d[100_000]) * int(d[1_000_000])
    end = time.perf_counter()
    print(f"{Solution} en {round(end-start,2)} secondes")
    print(f"The value is {Solution}")

    print(40*"-")
    print(f"Solution = {Solution}")
    print(40*"=")

if __name__ == "__main__":
    # execute only if run as a script
    main()
