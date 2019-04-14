Enonce = """
Summation of primes
Problem 10 
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

import EulerTools
import time

def main():
    print(40*"=")
    print(Enonce)
    print(40*"-")


    maxi = 2_000_000 #10
    start = time.perf_counter()
    Solution = 0
    for p in EulerTools.PrimeNumber(highest_value=maxi):
        Solution = Solution + p
    end = time.perf_counter()
    print(f"Solution={Solution} en {round(end-start,2)} secondes")

    print(f"The sum of all prime factors below {maxi} is {Solution}.")
    
    print(40*"-")
    print(f"Solution = {Solution}")
    print(40*"=")

if __name__ == "__main__":
    # execute only if run as a script
    main()
