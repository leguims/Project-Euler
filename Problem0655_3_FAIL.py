Enonce = """
Divisible Palindromes
Problem 655 
The numbers 545, 5995 and 15151 are the three smallest palindromes divisible by 109. There are nine palindromes less than 100000 which are divisible by 109.

How many palindromes less than 1032 are divisible by 10000019 ?
"""

class Palindrome:
  """Increment by start value and then check if it is a palindrome"""
  def __init__(self, max, start=1):
    self.max = max
    self.start = start

  def __iter__(self):
    self.value = self.start    # Real value of palindrome
    return self

  def __next__(self):
    self.value = self.value + self.start
    while(not self.isPalindrome(self.value)):
      self.value = self.value + self.start
      if self.value >= self.max :
        raise StopIteration
    return self.value

  def isPalindrome(self, number):
    number_str = str(number)
    #print(f"len(number_str)={len(number_str)} ; number_str={number_str} ; number_str[-1::-1]={number_str[-1::-1]}")
    return (len(number_str) >= 1) and (number_str == number_str[-1::-1])



def main():
    print(40*"=")
    print(Enonce)
    print(40*"-")
    
    import time
    
    digits = 10 #8 #32 #5
    divider = 1095 #109 #10_000_019 #109
    # Palindrome(pow(10, 12), {1095}): 9.653235062 secondes
    # Palindrome_3(pow(10, 12), {1095}): 1087.373263688 secondes
    
    print(f"Palindrome(pow(10, {digits}), {divider}):")
    start = time.perf_counter()
    Solution = 0
    for i in Palindrome(pow(10, digits), divider):
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
