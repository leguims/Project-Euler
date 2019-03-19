Enonce = """
Number letter counts

Problem 17
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""

# Iterator style
class countInWords:
    def __init__(self, start=1, end=1000):
        # English lesson to count : 
        # https://www.mathsisfun.com/numbers/counting-names-1000.html
        self.current = start
        self.currentWord = ''
        self.max = end
        self.wordConverter = {1:'one',
             2:'two',
             3:'three',
             4:'four',
             5:'five',
             6:'six',
             7:'seven',
             8:'eight',
             9:'nine',
             10:'ten',
             11:'eleven',
             12:'twelve',
             13:'thirteen',
             14:'fourteen',
             15:'fifteen',
             16:'sixteen',
             17:'seventeen',
             18:'eighteen',
             19:'nineteen',
             # 20 -> 99
             20:'twenty',
             30:'thirty',
             40:'forty',
             50:'fifty',
             60:'sixty',
             70:'seventy',
             80:'eighty',
             90:'ninety',
             }

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.max :
            raise StopIteration
        self.currentWord = self.convert(self.current)
        self.current = self.current + 1
        return self.currentWord

    def convert(self, number):
        if 1 <= number <= 20:
            return self.wordConverter[number]
        elif 21 <= number <= 99:
            word = self.wordConverter[number//10*10]
            if number%10:
                word = word + '-' + self.convert(number%10)
            return word
        elif 100 <= number <= 999:
            word = self.convert(number//100) + ' hundred'
            if number%100:
                word = word + ' and ' + self.convert(number%100)
            return word
        elif 1_000 <= number <= 999_999:
            word = self.convert(number//1000) + ' thousand'
            if number%1000:
                word = word + ', ' + self.convert(number%1000)
            return word
        elif 1_000_000 <= number <= 9_999_999:
            word = self.convert(number//1_000_000) + ' million'
            if number%1_000_000:
                word = word + ', ' + self.convert(number%1_000_000)
            return word
        elif 1_000_000_000 <= number <= 9_999_999_999:
            word = self.convert(number//1_000_000_000) + ' billion'
            if number%1_000_000_000:
                word = word + ', ' + self.convert(number%1_000_000_000)
            return word

def main():
    print(40*"=")
    print(Enonce)
    print(40*"-")

    Solution = 0
    start, end = 1, 1000 #115, 115 #342, 342 #1, 5
    for word in countInWords(start=start, end=end):
        print(f"{word}")
        Solution = Solution + len( word.replace(' ','').replace('-','') )

    print(f"{Solution} letters are used to count from {start} to {end}.")
    
    print(40*"-")
    print("Solution = {}".format(Solution))
    print(40*"=")

if __name__ == "__main__":
    # execute only if run as a script
    main()
