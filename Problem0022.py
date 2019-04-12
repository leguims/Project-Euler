Enonce = """
Names scores

Problem 22
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 x 53 = 49714.

What is the total of all the name scores in the file?
"""

def score(name):
    score = 0
    for i in name:
        score = score + ord(i) - ord('A') +1
    return score

def main():
    print(40*"=")
    print(Enonce)
    print(40*"-")

    with open('p022_names.txt', 'r') as myfile:
        unsorted_names = myfile.read()
    sorted_names = sorted(unsorted_names.replace('"','').split(','))
    print(sorted_names)
    
    #sorted_names = ['COLIN'] #sorted_names[:20]
    Solution = 0
    for index, name in enumerate(sorted_names, 1):
        Solution = Solution + index * score(name)
        
    print(f"The total of all the name scores in the file is {Solution}")
    
    print(40*"-")
    print(f"Solution = {Solution}")
    print(40*"=")

if __name__ == "__main__":
    # execute only if run as a script
    main()
