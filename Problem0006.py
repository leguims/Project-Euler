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

    sumOfSquare = sum([pow(i, 2) for i in range(1, max +1)])
    squareOfSum = pow(sum(range(1, max +1)), 2)
    Solution = difference = squareOfSum - sumOfSquare
    print(f"Sum Of Square of first {max} natural = {sumOfSquare}")
    print(f"Square Of Sum of first {max} natural = {squareOfSum}")
    
    print(40*"-")
    print("Solution = {}".format(Solution))
    print(40*"=")

if __name__ == "__main__":
    # execute only if run as a script
    main()
