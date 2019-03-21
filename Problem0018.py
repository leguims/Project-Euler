Enonce = """
Maximum path sum I

Problem 18
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

   3
  7 4
 2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

                        75
                      95 64
                    17 47 82
                   18 35 87 10
                 20 04 82 47 65
               19 01 23 75 03 34
              88 02 77 73 07 63 67
            99 65 04 28 06 16 70 92
          41 41 26 56 83 40 80 70 33
        41 48 72 33 47 32 37 16 94 29
      53 71 44 65 25 43 91 52 97 51 14
     70 11 33 28 77 73 17 78 39 68 17 57
   91 71 52 38 17 14 91 43 58 50 27 29 48
  63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)
"""

import EulerTools

def main():
    print(40*"=")
    print(Enonce)
    print(40*"-")

    triangle_string = """
                        75
                      95 64
                    17 47 82
                   18 35 87 10
                 20 04 82 47 65
               19 01 23 75 03 34
              88 02 77 73 07 63 67
            99 65 04 28 06 16 70 92
          41 41 26 56 83 40 80 70 33
        41 48 72 33 47 32 37 16 94 29
      53 71 44 65 25 43 91 52 97 51 14
     70 11 33 28 77 73 17 78 39 68 17 57
   91 71 52 38 17 14 91 43 58 50 27 29 48
  63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""
    
    #triangle_string = """
    #3
   #7 4
  #2 4 6
 #8 5 9 3
#"""
    
    
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
