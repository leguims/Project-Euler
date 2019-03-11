Enonce = """
Largest prime factor
Problem 3 
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

import EulerTools

# Iterator style
class PrimeNumber:
  def __init__(self, size=None, highest_value=None):
    self.current = 2
    self.index = size
    self.highest_value = highest_value

  def __iter__(self):
    return self

  def __next__(self):
    if self.index is not None:
        if self.index == 0 :
            raise StopIteration
        self.index = self.index - 1
    while(True):
      if self.highest_value is not None:
          if (self.highest_value < self.current) :
              raise StopIteration
      for multiple in range(2, self.current):
        if (self.current % multiple == 0) and (self.current != multiple):
          break
      else:
        self.current = self.current + 1
        return self.current - 1
      self.current = self.current + 1

def main():
    print(40*"=")
    print(Enonce)
    print(40*"-")

    import time

    Solution = set()
    number = 600_851_475_143  #13_195  
    reste = number
    start = time.perf_counter()
    for v in PrimeNumber(highest_value=number):
        while reste%v == 0:
          reste = reste/v
          Solution.add(v)
        if reste == 1:
          break
    end = time.perf_counter()
    print(f"{Solution} en {round(end-start,2)} secondes")
    print(f"List of prime factor of {number} : {Solution}")
    Solution = max(Solution)

    # With EulerTools
    Solution = set()
    number = 600_851_475_143  #13_195  
    reste = number
    start = time.perf_counter()
    for prime in EulerTools.PrimeFactor(highest_value=number):
        Solution.add(prime)
        #print(prime)
    end = time.perf_counter()
    print(f"{Solution} with EulerTools en {round(end-start,2)} secondes")
    print(f"List of prime factor of {number} : {Solution}")
    
    print(40*"-")
    print("Solution = {}".format(Solution))
    print(40*"=")

if __name__ == "__main__":
    # execute only if run as a script
    main()
