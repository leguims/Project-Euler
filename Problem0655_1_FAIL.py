Enonce = """
Divisible Palindromes
Problem 655 
The numbers 545, 5995 and 15151 are the three smallest palindromes divisible by 109. There are nine palindromes less than 100000 which are divisible by 109.

How many palindromes less than 1032 are divisible by 10000019 ?
"""

# Iterator style
class Palindrome:
  """Construct palindromes"""
  def __init__(self, max, start=1):
    self.max = max
    self.start = int( str(start)[:int(round(len(str(start))/2 + 0.1))] )

  def __iter__(self):
    self.odd = True   # number of digits is odd or not (even)
    self.base = self.start     # Half side of palindrome
    self.value = 1    # Real value of palindrome
    return self

  def __next__(self):
    string = str(self.base)
    if self.odd:
      self.value = int(string[:] + string[-2::-1]) # as 'abcba'
      # End if lower value is to high
      if self.value >= self.max:
        raise StopIteration
    else:
      self.value = int(string[:] + string[-1::-1]) #  as 'abccba'
      self.base = self.base + 1
    self.odd = not self.odd
    # value to high, return next odd value
    if self.value >= self.max:
      self.__next__()
    return self.value


def main():
    print(40*"=")
    print(Enonce)
    print(40*"-")
    
    import time
    
    digits = 11 #32 #5
    divider = 1095 #10_000_019 #109
    # Palindrome(pow(10, 12), {1095}): 9.653235062 secondes
    # Palindrome2(pow(10, 12), {1095}): 1087.373263688 secondes
    
    print(f"Palindrome(pow(10, {digits}), {divider}):")
    start = time.perf_counter()
    Solution = 0
    for i in Palindrome(pow(10, digits), divider):
      if (i % divider) == 0:
        #print(i)
        Solution = Solution + 1
    end = time.perf_counter()
    print(f"{Solution} en {round(end-start, 3)} secondes")
    #print(f"{Solution}")
    
    print(40*"-")
    print(f"There are {Solution} palindromes less than 10^{digits} and divisible by {divider}")
    print(40*"=")

if __name__ == "__main__":
    # execute only if run as a script
    main()
