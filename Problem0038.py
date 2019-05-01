Enonce = """
Pandigital multiples

Problem 38
Take the number 192 and multiply it by each of 1, 2, and 3:

192 x 1 = 192
192 x 2 = 384
192 x 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?
"""

import EulerTools
import time

def main():
    print(40*"=")
    print(Enonce)
    print(40*"-")
    
    Solution = 0
    maxi = 9_999 #200 #9_999
    start = time.perf_counter()
    for i in range(1, maxi+1):
        concatenate_product = ""
        for m in range(1, 11):
            concatenate_product += str(i*m)
            if len(concatenate_product) >= 9:
                break
        if len(concatenate_product) != 9:
            continue
        for integer in range(1, 10):
            if str(integer) not in concatenate_product:
                break
        else:
            print(f"pandigital 9-digit : {concatenate_product} is formed by concatenated product {i} x {list(range(1, m+1))}")
            if int(concatenate_product) > Solution:
                Solution = int(concatenate_product)
                print(f" *** New Max !!! *** ")
    end = time.perf_counter()
    print(f"{Solution} en {round(end-start,2)} secondes")
    print(f"Largest 1 to 9 pandigital 9-digit number is {Solution}")

    print(40*"-")
    print(f"Solution = {Solution}")
    print(40*"=")

if __name__ == "__main__":
    # execute only if run as a script
    main()
