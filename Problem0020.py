Enonce = """
Factorial digit sum

Problem 20
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""

from math import factorial

def main():
    print(40*"=")
    print(Enonce)
    print(40*"-")
    
    Solution = 0
    size = 100 #10
    for a in str(factorial(size)):
        Solution = Solution + int(a)
    
    print(f"Sum of digits in the number {size}! is {Solution}")
    
    print(40*"-")
    print("Solution = {}".format(Solution))
    print(40*"=")

if __name__ == "__main__":
    # execute only if run as a script
    main()
