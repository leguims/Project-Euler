Enonce = """
Sum square difference
Problem 6 
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

def main():
    print(40*"=")
    print(Enonce)
    print(40*"-")

    max = 100 #10

    print(f" * Brute force implementation : ")
    sumOfSquare = sum([pow(i, 2) for i in range(1, max +1)])
    squareOfSum = pow(sum(range(1, max +1)), 2)
    difference = squareOfSum - sumOfSquare
    print(f"Sum Of Square of first {max} natural = {sumOfSquare}")
    print(f"Square Of Sum of first {max} natural = {squareOfSum}")
    print(f"Difference = {difference}")

    print("""
 * Smart implementation : 
Square Of Sum = (1+2+3...+N)^2 = 1^2+2^2+3^2+...+N^2+ 2x(1x2 + 1x3 +...+ 1xN + 2x3 + ... + 2xN + 3x4 + ... + 3xN + ... + (N-1)xN)
Sum Of Square = 1^2+2^2+3^2+...+N^2
Square Of Sum - Sum Of Square = 2x(1x2 + 1x3 +...+ 1xN + 2x3 +...+ 2xN + 3x4 +...+ 3xN +...+ (N-1)xN)
Square Of Sum - Sum Of Square = 2x( SUM[M=1;N-1](M x SUM[S=M+1;N](S)))

Solution =  2x( SUM[M=1;N-1](M x SUM[S=M+1;N](S)))
""")
    Solution = 0
    for M in range(1, max):
        for S in range(M+1, max+1):
            Solution = Solution + M*S
    Solution = 2 * Solution

    if difference != Solution:
        print("'Brute force' implementation is different then 'Smart' implementation !!")
    
    print(40*"-")
    print(f"Solution = {Solution}")
    print(40*"=")

if __name__ == "__main__":
    # execute only if run as a script
    main()
