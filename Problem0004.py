Enonce = """
Largest palindrome product
Problem 4 
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

# Iterator style
class Product:
  def __init__(self, size=2):
    if size >= 2:
      self.size = size
    else:
      self.size = 2
    self.factors = [int(self.size*'9'), int(self.size*'9')]

  def __iter__(self):
    return self

  def __next__(self):
    if self.factors == [0, 0] :
        raise StopIteration
    product, factor1, factor2 = self.factors[0]*self.factors[1], self.factors[0], self.factors[1]
    # next values
    if self.factors[0] == 0 :
      self.factors[0] = self.factors[1] = self.factors[1]-1
    else:
      self.factors[0] = self.factors[0] - 1
    return product, factor1, factor2

def isPalindrome(number):
  #print(f"len(str(number))={len(str(number))} ; str(number)={str(number)} ; str(number)[-1::-1]={str(number)[-1::-1]}")
  return (len(str(number)) > 1) and (str(number) == str(number)[-1::-1])

def main():
    print(40*"=")
    print(Enonce)
    print(40*"-")

    #import time
    
    #start = time.perf_counter()
    #Solutions = {}
    #Solution = []
    #digits = 3 #2
    #for product, factor1, factor2 in Product(digits):
      #if isPalindrome(product):
        ##print(f"{factor1} x {factor2} = {product} is a palindrome)")
        #Solutions[product] = [product, factor1, factor2]
        #Solution.append(product)
    #product, factor1, factor2 = Solutions[max(Solution)]
    #Solution = f"{factor1} x {factor2} = {product} is the highest palindrome with {digits} digits)"
    #end = time.perf_counter()
    #print(f"{Solution} en {end-start} secondes")
    
    #start = time.perf_counter()
    Solution = [0, 0, 0]
    digits = 3 #2
    for product, factor1, factor2 in Product(digits):
      if (product > Solution[0]) and isPalindrome(product):
        Solution = [product, factor1, factor2]
    product, factor1, factor2 = Solution
    Solution = f"{factor1} x {factor2} = {product} is the highest palindrome with {digits} digits)"
    #end = time.perf_counter()
    #print(f"{Solution} en {end-start} secondes")
    print(f"{Solution}")

    print(40*"-")
    print("Solution = {}".format(Solution))
    print(40*"=")

if __name__ == "__main__":
    # execute only if run as a script
    main()
