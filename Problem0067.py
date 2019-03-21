Enonce = """
Maximum path sum II

Problem 67
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this problem, as there are 299 altogether! If you could check one trillion (1012) routes every second it would take over twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)
"""

import EulerTools

def main():
    print(40*"=")
    print(Enonce)
    print(40*"-")

    with open('p067_triangle.txt', 'r') as myfile:
        triangle_string = myfile.read()
    
    triangle = [[int(i) for i in l if i] for l in [i.strip().split() for i in triangle_string.split('\n') if i.strip()]]
    print(f"Triangle :")
    for line in triangle:
        print(line)
    
    cumulative_sum = list()
    path_numbers = list()
    #print(f"range(-1,-len(triangle)-1,-1)={list(range(-1,-len(triangle)-1,-1))}")
    for line in range(-1,-len(triangle)-1,-1):
        tmp_line = list()
        tmp_path = list()
        #print(f"range(len(triangle[line])-1)={list(range(len(triangle[line])-1))}")
        if not range(len(triangle[line])-1):
            maxi = triangle[line][0]+cumulative_sum[-1][0]
            number = path_numbers[-1][0] + [triangle[line][0]]
            tmp_line.append(maxi)
            tmp_path.append(number)
        else:
            for column in range(len(triangle[line])-1):
                if line != -1:
                    maxi = max(triangle[line][column]+cumulative_sum[-1][column], triangle[line][column+1]+cumulative_sum[-1][column+1])
                    number = path_numbers[-1][column] + [triangle[line][column]] if triangle[line][column]+cumulative_sum[-1][column] == maxi else path_numbers[-1][column+1] + [triangle[line][column+1]]
                else:
                    maxi = max(triangle[line][column], triangle[line][column+1])
                    number = [triangle[line][column]] if triangle[line][column] == maxi else [triangle[line][column+1]]
                tmp_line.append(maxi)
                tmp_path.append(number)
        cumulative_sum.append(tmp_line)
        path_numbers.append(tmp_path)
        #print(20*'-')
        #print(cumulative_sum)
        #print(20*'=')
        #print(path_numbers)
    Solution = cumulative_sum[-1]
    
    print(f"The greatest sum in triangle is {Solution} with sum of {path_numbers[-1]}")
    
    print(40*"-")
    print(f"Solution = {Solution}")
    print(40*"=")

if __name__ == "__main__":
    # execute only if run as a script
    main()
