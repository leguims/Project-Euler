Enonce = """
Palindrome-containing strings
Problem 486 
Let F5(n) be the number of strings s such that:

s consists only of '0's and '1's,
s has length at most n, and
s contains a palindromic substring of length at least 5.
For example, F5(4) = 0, F5(5) = 8, F5(6) = 42 and F5(11) = 3844.

Let D(L) be the number of integers n such that 5 ≤ n ≤ L and F5(n) is divisible by 87654321.

For example, D(107) = 0 and D(5·109) = 51.

Find D(1018).
"""

from multiprocessing import Pool
from multiprocessing import cpu_count
import json

# Iterator style
class Base2Palindrome:
  """Construct palindromes for base 2 between start and end values with size digits"""
  def __init__(self, start = 1, end = 1, size = 1):
    self.start = start
    self.end = end
    self.size = size

  def __iter__(self):
    self.value = self.start  # Value
    return self

  def __next__(self):
    while(True):
      if self.value >= self.end:
        raise StopIteration
      value_str = "{0:0{size}b}".format(self.value, size=self.size)
      self.value = self.value + 1
      if value_str == value_str[-1::-1] :
        return value_str

def F5(n = 1):
  # Count all palindromes at least 5 !
  size = n
  end = pow(2, n)
  palindrome5 = list(Base2Palindrome(0, pow(2, 5), 5))
  palindrome6 = list(Base2Palindrome(0, pow(2, 6), 6))
  # all possible palindrome inside a string
  a=[list(Base2Palindrome(0, pow(2, i), i)) for i in range(5, n+1)]
  palindromes = []
  for b2p in [list(Base2Palindrome(0, pow(2, i), i)) for i in range(5, n+1)]:
    palindromes = palindromes + b2p
  #palindromes = sum([list(Base2Palindrome(0, pow(2, i), i)) for i in range(5, n+1)])
  value = 0
  count = 0
  while(True):
    if value >= end:
      return count
    value_str = "{0:0{size}b}".format(value, size = size)
    value = value + 1
    for p in palindromes :
      pos = 0
      # find overlapping palidromes
      while (pos != -1) and (pos < len(p)):
        pos = value_str.find(p, pos)
        if pos != -1:
          count = count + 1
          pos = pos + 1
      #if p in value_str:
        #count = count + 1
        ##break

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
    
    print(f"F5(4)={F5(4)}")
    print(f"F5(5)={F5(5)}")
    print(f"F5(6)={F5(6)}") # 40 instead of 42 ?!
    print(f"F5(7)={F5(7)}")
    print(f"F5(11)={F5(11)}") # 7328 instead of 3844 !?
    import time
    
    digits = 6 #32 #10 #32 #5
    file_prefix = 'Problem0486_'+str(digits)

    #print(f"f_Base10Base2Palindrome(pow(10, {digits})):")
    #start = time.perf_counter()
    #Solution = 0
    #counter = 0
    #args = [(pow(10, min), pow(10, min+2)) for min in range(0, digits, 2)]
    #args.reverse() # First works will be the longer
    #with Pool(cpu_count()) as p:
      #for palidromes in p.imap_unordered(f_Base10Base2Palindrome, args):
        ##print(f"Palidromes = {palidromes}")
        #Solution = Solution + sum( palidromes )
        #counter = counter + 1
        #print(f"Actuellement, Somme={Solution} ... ({counter}/{len(args)} soit {round(100*counter/len(args))}% achevÃ©es)")
        #with open(file_prefix+'_Solution.txt', 'a') as outfile:  
          #print(f"Actuellement Somme={Solution} ... ({counter}/{len(args)} soit {round(100*counter/len(args))}% achevÃ©es)", file=outfile)
        #with open(file_prefix+'_Solution_details.txt', 'a') as outfile:  
          #json.dump(palidromes, outfile)
          #print(f"\nActuellement Somme={Solution} ... ({counter}/{len(args)} soit {round(100*counter/len(args))}% achevÃ©es)\n", file=outfile)
    #end = time.perf_counter()
    #print(f"Solution={Solution} en {round(end-start, 3)} secondes")
    ##print(f"{Solution}")
    
    print(40*"-")
    #print(f"Sum of double base palindromes less than 10^{digits} is {Solution}")
    print(40*"=")

if __name__ == "__main__":
    # execute only if run as a script
    main()
