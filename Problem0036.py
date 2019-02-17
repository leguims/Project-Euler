Enonce = """
Double-base palindromes
Problem 36 
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""

from multiprocessing import Pool
from multiprocessing import cpu_count
import json

# Iterator style
class Palindrome:
  """Construct palindromes for base 10 between start and end values"""
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
class Base10Base2Palindrome:
  """Construct palindromes for base 10 and 2"""
  def __init__(self, start = 1, end = 1):
    self.palindrome = Palindrome(start, end)

  def __iter__(self):
    self.palindrome.__iter__()
    return self

  def __next__(self):
    while(True):
      value = self.palindrome.__next__()
      value_binary_string = "{0:b}".format(value)
      if value_binary_string == value_binary_string[-1::-1] :
        return value

def f_Base10Base2Palindrome(*args):
  if len(args) == 1:
    args = args[0]
  if len(args) == 2:
    return [p for p in Base10Base2Palindrome(args[0], args[1])]
  else:
    return 0

def main():
    print(40*"=")
    print(Enonce)
    print(40*"-")
    
    import time
    
    digits = 6 #32 #10 #32 #5
    file_prefix = 'Problem0036_'+str(digits)

    print(f"f_Base10Base2Palindrome(pow(10, {digits})):")
    start = time.perf_counter()
    Solution = 0
    counter = 0
    args = [(pow(10, min), pow(10, min+2)) for min in range(0, digits, 2)]
    args.reverse() # First works will be the longer
    with Pool(cpu_count()) as p:
      for palidromes in p.imap_unordered(f_Base10Base2Palindrome, args):
        #print(f"Palidromes = {palidromes}")
        Solution = Solution + sum( palidromes )
        counter = counter + 1
        print(f"Actuellement, Somme={Solution} ... ({counter}/{len(args)} soit {round(100*counter/len(args))}% achevées)")
        with open(file_prefix+'_Solution.txt', 'a') as outfile:  
          print(f"Actuellement Somme={Solution} ... ({counter}/{len(args)} soit {round(100*counter/len(args))}% achevées)", file=outfile)
        with open(file_prefix+'_Solution_details.txt', 'a') as outfile:  
          json.dump(palidromes, outfile)
          print(f"\nActuellement Somme={Solution} ... ({counter}/{len(args)} soit {round(100*counter/len(args))}% achevées)\n", file=outfile)
    end = time.perf_counter()
    print(f"Solution={Solution} en {round(end-start, 3)} secondes")
    #print(f"{Solution}")
    
    print(40*"-")
    print(f"Sum of double base palindromes less than 10^{digits} is {Solution}")
    print(40*"=")

if __name__ == "__main__":
    # execute only if run as a script
    main()
