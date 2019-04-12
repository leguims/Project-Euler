Enonce = """
Digit factorials

Problem 34
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""

import EulerTools
import math

def main():
    print(40*"=")
    print(Enonce)
    print(40*"-")
    
    # find max possible digits
    max_number = 10
    for digits in range(2, 100):
        if math.log10(math.factorial(9)*digits) < (digits-1):
            break
        max_number = math.factorial(9)*digits
    print(f"Maximum possible number = {max_number}")

    # find solution
    size = 2
    Solution = 0  
    for number in range (10, max_number+1):
        _sum = 0
        for digit in str(number):
            _sum += math.factorial( int(digit) )
            if _sum > number:
                break
        if _sum == number:
            print(f"{number} is equal to the sum of the factorial of their digits.")
            Solution += number

    print(f"The sum of all numbers which are equal to the sum of the factorial of their digits is {Solution}")
    
    print(40*"-")
    print(f"Solution = {Solution}")
    print(40*"=")

if __name__ == "__main__":
    # execute only if run as a script
    main()
