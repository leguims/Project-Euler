Enonce = """
Divisible Palindromes
Problem 655 
The numbers 545, 5995 and 15151 are the three smallest palindromes divisible by 109. There are nine palindromes less than 100000 which are divisible by 109.

How many palindromes less than 1032 are divisible by 10000019 ?
"""

import math
#import operator
import functools

# Iterator style
class Palindrome:
  """Construct palindromes"""
  def __init__(self, max, divider=1):
    self.max = max
    self.divider = divider
    
  def gcd(self, *args):
    """As math.gcd for more than 2 arguments"""
    if len(args) == 2:
      return math.gcd(args[0], args[1])
    elif len(args) == 1:
      return args[0]
    return math.gcd(args[0], self.gcd(*args[1:]))

  def __iter__(self):
    self.equation = []
    self.next = True
    self.odd = True
    self.max_digits = len(str(self.max - 1))
    pound_sum = 0
    for i in range( round( self.max_digits /2 +0.1 ) ):
      if (self.max_digits-1 -i) != i :
        pound = pow(10, self.max_digits-1 -i) + pow(10, i)
        pound_sum = pound_sum + pound
        #self.equation.append( pound % self.divider )
        self.equation.append( pound )
      else:
        pound = pow(10, i)
        pound_sum = pound_sum + pound
        #self.equation.append( pound % self.divider )
        self.equation.append( pound )
        self.odd = False
        
    # Sum of pounds < divider ==> cannot be divided by it
    if pound_sum < self.divider:
      # End of iterator
      self.next = False
      return self
    
    self.size_equation = len(self.equation)
    
    #_gcd = self.gcd(*self.equation)
    #if _gcd > 1:
      #for i, v in enumerate(self.equation):
        #self.equation[i] = self.equation[i] // _gcd
    
    self.factors = [1]+[0]*(self.size_equation -1)
    #self.incrementFactors()
    self.setValue()
    return self

  def incrementFactors(self):
    max_index = len(self.factors) - 1
    for i, v in enumerate(self.factors):
      if self.factors[max_index - i] < 9:
        self.factors[max_index - i] = self.factors[max_index - i] + 1
        return
      else:
        self.factors[max_index - i] = 0
    raise StopIteration
    
  def setValue(self):
    if self.odd :
      self.value = functools.reduce( lambda x, y: 10*x + y, self.factors + self.factors[-1::-1] )
    else:
      self.value = functools.reduce( lambda x, y: 10*x + y, self.factors[:] + self.factors[-2::-1] )
    
  def __next__(self):
    if not self.next:
      raise StopIteration
    
    while(True):
      self.setValue()
      if self.value >= self.max:
        raise StopIteration
      
      # result = SOMME ( self.factors x self.equation[i] )
      result = functools.reduce( lambda x, y: x + y[0]*y[1], zip(self.factors, self.equation), 0)
      
      if (result % self.divider) == 0:
        self.setValue()
        if self.value >= self.max:
          raise StopIteration
        else:
          self.incrementFactors()
          return self.value
      
      self.incrementFactors()


def main():
    print(40*"=")
    print(Enonce)
    print(40*"-")
    
    import time
    
    digits = 10 #8
    divider = 1095 #109
    
    print(f"Palindrome(pow(10, {digits}), {divider}):")
    start = time.perf_counter()
    Solution = 0
    for digit in range(1, digits+1):
      print(f"Palindrome(pow(10, {digit}), {divider})")
      for i in Palindrome(pow(10, digit), divider):
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
