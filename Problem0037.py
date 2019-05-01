Enonce = """
Truncatable primes

Problem 37
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

import EulerTools
import math
import time

def main():
    print(40*"=")
    print(Enonce)
    print(40*"-")
    
    Solution = set()
    maxi = 100_000_000 #10_000 #1_000_000
    start = time.perf_counter()
    for prime in EulerTools.PrimeNumber(highest_value=maxi):
        if prime < 10:
            continue
        prime_str = str(prime)
        pl = [int(prime_str[i:]) for i in range(len(prime_str))]
        pr = [int(prime_str[0:i+1]) for i in range(len(prime_str))]
        is_prime = [EulerTools.isPrimeNumber(p) for p in pl+pr]
        if all(is_prime):
            print(f"prime={prime}")
            #print(f"Solution was  = {Solution}")
            # Remove to low solutions
            Solution = Solution.difference(pl+pr)
            Solution.add(prime)
            print(f"Solution is now {Solution}")
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
