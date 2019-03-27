Enonce = """
1000-digit Fibonacci number

Problem 25
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn-1 + Fn-2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""

import EulerTools

def main():
    print(40*"=")
    print(Enonce)
    print(40*"-")

    Solution = 0
    size = 1000 #3
    highest = int('9'*size)
    for index, fibo_value in enumerate(EulerTools.Fibonacci(highest_value=highest),1):
        #print(f"Fibo({index})={fibo_value}")
        if len(str(fibo_value)) >= size:
            Solution = index + 1 # F1=1 ; F2=1 instead of F1=1 ; F2=2
            break
    
    print(f"The {Solution}th Fibonacci value is {len(str(fibo_value))} digits")
    
    print(40*"-")
    print("Solution = {}".format(Solution))
    print(40*"=")

if __name__ == "__main__":
    # execute only if run as a script
    main()
