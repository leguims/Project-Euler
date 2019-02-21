Enonce = """
Special Pythagorean triplet
Problem 9 
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

import math

def main():
    print(40*"=")
    print(Enonce)
    print(40*"-")


    maxi = 1000
    Pythagorean = []
    #count = 0
    c_min = math.ceil(maxi/3)
    for c in range(c_min, maxi):
        #count += 1
        b_min = math.ceil((maxi - c)/2) if ((maxi - c)%2)!=0 else int((maxi - c)/2 + 1)
        for b in range( b_min , min(c, maxi - c)):
            #count += 1
            a = maxi - b - c
            #print(f"{a} < {b} < {c}")
            if a >= b:
                print(f"oups {a} < {b} < {c}")
                continue
            if (pow(a, 2) + pow(b, 2)) == pow(c, 2):
                Pythagorean.append([a, b, c])
                print(f"Pythagorean triplet found : {a} < {b} < {c}")

    #print(count)

    if len(Pythagorean) > 0:
        a, b, c = Pythagorean[0]
        Solution = a * b * c

    print(f"The Pythagorean triplet for which a + b + c = 1000 is Pythagorean[0].")
    
    print(40*"-")
    print(f"Solution = {Solution}")
    print(40*"=")

if __name__ == "__main__":
    # execute only if run as a script
    main()
