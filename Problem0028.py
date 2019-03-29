Enonce = """
Number spiral diagonals

Problem 28
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""

import EulerTools

def main():
    print(40*"=")
    print(Enonce)
    print(40*"-")

    size = 1001 #5 #3
    Solution = 1
    current = 1
    for s in range(2, size, 2):
        Solution = Solution + current * 4 + s*10 # <=> (current + size) + (current + 2*size) + (current + 3*size) + (current + 4*size)
        current = current + s * 4
    
    print(f"The sum of the numbers on the diagonals in a {size} by {size} spiral formed is {Solution} ")
    
    print(40*"-")
    print("Solution = {}".format(Solution))
    print(40*"=")

if __name__ == "__main__":
    # execute only if run as a script
    main()
