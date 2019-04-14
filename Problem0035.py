Enonce = """
Circular primes

Problem 35
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""

import EulerTools
import math
import time

def main():
    print(40*"=")
    print(Enonce)
    print(40*"-")
    
    Solution = set()
    maxi = 1_000_000 #100  
    start = time.perf_counter()
    for prime in EulerTools.PrimeNumber(highest_value=maxi):
        c = EulerTools.isCircularPrime(prime)
        if (c['isCircularPrime']) and (prime not in Solution):
            Solution = Solution.union(c['CircularPrimeList'])
        #print(f"prime={prime} : isCircularPrime={c['isCircularPrime']}, CircularPrimeList={c['CircularPrimeList']}")
    end = time.perf_counter()
    print(f"{Solution} en {round(end-start,2)} secondes")
    print(f"List of circular prime under {maxi} : {Solution}")

    print(f"There are {len(Solution)} circular primes below {maxi}")
    
    print(40*"-")
    print(f"Solution = {Solution}")
    print(40*"=")

if __name__ == "__main__":
    # execute only if run as a script
    main()
