Enonce = """
Integer right triangles

Problem 39
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p <= 1000, is the number of solutions maximised?
"""

import EulerTools
import time

def main():
    print(40*"=")
    print(Enonce)
    print(40*"-")
    
    Solution = {'perimeter': 0, 'number of solution': 0}
    maxi = 1_000 #120 
    start = time.perf_counter()
    for perimeter  in range(4, maxi+1):
        solution_number = 0
        # h as hypotenus
        for hypotenus in range(2, perimeter-2+1):
            for a in range((perimeter - hypotenus)//2, perimeter - hypotenus):
                b = perimeter -hypotenus -a
                if (a*a + b*b) == (hypotenus*hypotenus):
                    # right angle triangle
                    solution_number += 1
                    #print(f"Current solution is perimeter {perimeter} with a={a} b={b} and hypotenus={hypotenus}.")
        if solution_number > Solution['number of solution']:
            Solution['perimeter'] = perimeter
            Solution['number of solution'] = solution_number
            print(f"Current best solution is perimeter {Solution['perimeter']} with {Solution['number of solution']} solutions.")
    end = time.perf_counter()
    print(f"{Solution['perimeter']} en {round(end-start,2)} secondes")
    print(f"The maximised number of solutions is for p={Solution['perimeter']} with {Solution['number of solution']} solutions")

    print(40*"-")
    print(f"Solution = {Solution['perimeter']}")
    print(40*"=")

if __name__ == "__main__":
    # execute only if run as a script
    main()
