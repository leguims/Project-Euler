Enonce = """
Power digit sum

Problem 16
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""

def main():
    print(40*"=")
    print(Enonce)
    print(40*"-")
    
    Solution = 0
    size = 1000 #15
    for a in str(pow(2,size)):
        Solution = Solution + int(a)
    
    print(f"Sum of digits of 2 power 1000 is {Solution}")
    
    print(40*"-")
    print("Solution = {}".format(Solution))
    print(40*"=")

if __name__ == "__main__":
    # execute only if run as a script
    main()
