Enonce = """
Digit cancelling fractions

Problem 33
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
"""

import EulerTools

def main():
    print(40*"=")
    print(Enonce)
    print(40*"-")

    # find solution
    size = 2
    fractions = list()
    for num in range (10, 100):
        for den in range (10, 100):
            if num >= den:
                continue
            for c in str(num):
                if c is '0':
                    continue
                if c in str(den):
                    try:
                        if num/den == int(str(num).replace(c,''))/int(str(den).replace(c,'')):
                            print(f"{num}/{den}")
                            fractions.append({'num': num, 'den': den})
                    except:
                        pass
    
    # Simplify solution
    print(fractions)
    Solution = {'num': 1, 'den': 1}
    for f in fractions:
        Solution['num'] *= f['num']
        Solution['den'] *= f['den']
    print(f"Solution = {Solution['num']}/{Solution['den']}")
    for pf in EulerTools.PrimeFactor(highest_value=Solution['num']):
        #print(f"pf={pf} : {Solution['num']}/{Solution['den']}")
        while (Solution['num'] % pf) == 0 and (Solution['den'] % pf) == 0:
            Solution['num'] //= pf
            Solution['den'] //= pf
            #print(f"{Solution['num']}/{Solution['den']}")
    print(f"Solution in its lowest common terms = {Solution['num']}/{Solution['den']}")
    
    print(40*"-")
    print(f"Solution = {Solution['num']}/{Solution['den']}")
    print(40*"=")

if __name__ == "__main__":
    # execute only if run as a script
    main()
