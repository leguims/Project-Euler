Enonce = """
10001st prime
Problem 7 
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

import EulerTools

# Iterator style
class PrimeNumber:
  def __init__(self, rank=1):
    self.current = 2
    self.index = rank

  def __iter__(self):
    return self

  def __next__(self):
    if self.index == 0 :
        raise StopIteration
    self.index = self.index - 1
    while(True):
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
    rank = 10_001 #6  
    
    # About 3mins !
    start = time.perf_counter()
    for prime in PrimeNumber(rank):
        #print(prime)
        pass
    end = time.perf_counter()
    Solution = prime
    print(f"{Solution} en {round(end-start,2)} secondes")
    print(f"The {rank}th prime number is {Solution}")
    
    # About 3s !
    start = time.perf_counter()
    for prime in EulerTools.PrimeNumber(rank = rank):
        #print(prime)
        pass
    end = time.perf_counter()
    Solution = prime
    print(f"{Solution} en {round(end-start,2)} secondes")
    print(f"The {rank}th prime number is {Solution}")
    
    print(40*"-")
    print(f"Solution = {Solution}")
    print(40*"=")

if __name__ == "__main__":
    # execute only if run as a script
    main()
