Enonce = """
Divisible Palindromes
Problem 655 
The numbers 545, 5995 and 15151 are the three smallest palindromes divisible by 109. There are nine palindromes less than 100000 which are divisible by 109.

How many palindromes less than 1032 are divisible by 10000019 ?
"""

from multiprocessing import Pool
from multiprocessing import cpu_count
import json

# Iterator style
class Palindrome:
  """Construct palindromes between start and end values"""
  def __init__(self, start = 1, end = 1):
    self.start = start
    self.end = end

  def __iter__(self):
    self.odd = True         # number of digits is odd or not (even)
    self.base = int( str(self.start)[:int(round(len(str(self.start))/2 + 0.1))] )  # Half side of palindrome
    self.value = self.start # Real value of palindrome
    return self

  def __next__(self):
    string = str(self.base)
    if self.odd:
      self.value = int(string[:] + string[-2::-1]) # as 'abcba'
      # End if lower value is to high
      if self.value >= self.end:
        raise StopIteration
    else:
      self.value = int(string[:] + string[-1::-1]) #  as 'abccba'
      self.base = self.base + 1
    self.odd = not self.odd
    # value to high, return next odd value
    if (self.value < self.start) or (self.value >= self.end) :
      self.__next__()
    return self.value

# Iterator style
class DivisiblePalindrome:
  """Construct divisible palindromes"""
  def __init__(self, start = 1, end = 1, divider = 1):
    self.divider = divider
    self.palindrome = Palindrome(start, end)

  def __iter__(self):
    self.palindrome.__iter__()
    return self

  def __next__(self):
    while(True):
      value = self.palindrome.__next__()
      if ( value % self.divider) == 0 :
        return value

def f_DivisiblePalindrome(*args):
  if len(args) == 1:
    args = args[0]
  if len(args) == 3:
    return [p for p in DivisiblePalindrome(args[0], args[1], args[2])]
  else:
    return 0

def main():
    print(40*"=")
    print(Enonce)
    print(40*"-")
    
    import time
    
    digits = 32 #10 #32 #5
    divider = 110_000_019 #1095 #110_000_019 #109
    file_suffix = '_'+str(digits)+'_'+str(divider)

    print(f"Palindrome({divider}, pow(10, {digits}), {divider}):")
    start = time.perf_counter()
    Solution = 0
    counter = 0
    args = [(pow(10, min), pow(10, min+2), divider) for min in range(0, digits, 2) if pow(10, min+2) >= divider]
    args.reverse() # First works will be the longer
    with Pool(cpu_count()) as p:
      for palidromes in p.imap_unordered(f_DivisiblePalindrome, args):
        #print(f"Palidromes = {palidromes}")
        Solution = Solution + len( palidromes )
        counter = counter + 1
        print(f"Actuellement {Solution} solutions trouvées... ({counter}/{len(args)} soit {round(100*counter/len(args))}% achevé)")
        with open('Problem0655'+file_suffix+'_Solution.txt', 'a') as outfile:  
          print(f"Actuellement {Solution} solutions trouvées... ({counter}/{len(args)} soit {round(100*counter/len(args))}% achevé)", file=outfile)
        with open('Problem0655'+file_suffix+'_Solution_details.txt', 'a') as outfile:  
          json.dump(palidromes, outfile)
          print(f"\nActuellement {Solution} solutions trouvées... ({counter}/{len(args)} soit {round(100*counter/len(args))}% achevé)\n", file=outfile)
    end = time.perf_counter()
    print(f"{Solution} solutions en {round(end-start, 3)} secondes")
    #print(f"{Solution}")
    
    print(40*"-")
    print(f"There are {Solution} palindromes less than 10^{digits} and divisible by {divider}")
    print(40*"=")

if __name__ == "__main__":
    # execute only if run as a script
    main()
