Enonce = """
Pandigital prime

Problem 41
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""

import EulerTools
import time

def main():
    print(40*"=")
    print(Enonce)
    print(40*"-")
    
    # Méthode brute : Parcourir tous les nombres pandigitaux et trouver le plus gros premier.
    maxi_pandigital = 9_876_543_210
    max_pandigital_prime = None
    start = time.perf_counter()
    for pandigital in EulerTools.Pandigital(end=maxi_pandigital, reverse=True):
        if EulerTools.isPrimeNumber(pandigital):
            max_pandigital_prime = pandigital
            break
    
    
    Solution = max_pandigital_prime
    end = time.perf_counter()
    print(f"{Solution} en {round(end-start,2)} secondes")
    print(f"The value is {Solution}")

    print(40*"-")
    print(f"Solution = {Solution}")
    print(40*"=")

if __name__ == "__main__":
    # execute only if run as a script
    main()
