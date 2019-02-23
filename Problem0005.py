Enonce = """
Smallest multiple
Problem 5 
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

def main():
    print(40*"=")
    print(Enonce)
    print(40*"-")

    import time

    print(""" Solution can be divided by 1 to 20:
2x2x3x3 = divided by 3, 6, 9, 12 and 18
2x2x2x2 = divided by 2, 4, 8 and 16
2x2x3x5 = divided by 5, 10, 15, 20
2x7 = divided by 7, 14
11, 13, 17, 19 = prime factor

Solution = 2*2*2*2*3*3*5*7*11*13*17*19
""")
    Solution = 2*2*2*2*3*3*5*7*11*13*17*19
    for i in range(1, 21):
        if (Solution % i) == 0:
            print(f"{Solution}/{i} = {Solution//i}")
        else:
            print(f"{Solution} cannot be divided by {i}")
    
    print(40*"-")
    print("Solution = {}".format(Solution))
    print(40*"=")

if __name__ == "__main__":
    # execute only if run as a script
    main()
