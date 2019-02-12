Enonce = """
Neighbourly Constraints
Problem 654 
Let T(n,m) be the number of m-tuples of positive integers such that the sum of any two neighbouring elements of the tuple is ≤ n.

For example, T(3,4)=8, via the following eight 4-tuples:
(1,1,1,1)
(1,1,1,2)
(1,1,2,1)
(1,2,1,1)
(1,2,1,2)
(2,1,1,1)
(2,1,1,2)
(2,1,2,1)

You are also given that T(5,5)=246, T(10,10^2)≡862820094(mod1000000007) and T(10^2,10)≡782136797(mod1000000007).

Find T(5000,10^12)mod1000000007.
"""

from itertools import product, chain
from operator import add

# Iterator style
class T: # Works well, but take time.
  def __init__(self, n=1, m=1):
    self.n = n if n>0 else 1
    self.m = m if m>0 else 1

  def __iter__(self):
    self.current = [self.n-1]*self.m
    return self

  def increaseCurrent(self):
    #print(f"current = {self.current}")
    for i in range(self.m):
      if self.current[i] > 1 :
        self.current[i] = self.current[i] - 1
        return
      elif i < self.m :
        # Reset value and decrement next index
        self.current[i] = self.n-1
    
  def lastIter(self):
    # Last value to treat is [1]*self.m
    return self.current == [1]*self.m
    
  def __next__(self):
    if self.current == None :
      raise StopIteration
    while(True):
      for i in range(self.m-1):
        if (self.current[i]+self.current[i+1]) > self.n:
          break
      else:
        result = tuple(self.current)
        if not self.lastIter():
          self.increaseCurrent()
        else:
          # End of itarable
          self.current = None
        return result
      if not self.lastIter():
        self.increaseCurrent()
      else:
        raise StopIteration
    

# Iterator style
class T_new: # Works well, but take time.
  def __init__(self, n=1, m=1):
    self.n = n if n>0 else 1
    self.m = m if m>0 else 1
  
  def create_valid_2tuples(self):
    # List all 2-Tuple valid with 'n'
    self.valid_2tuples = []
    for i in product(range(1,self.n),repeat=2):
      if sum(i) <= self.n :
        self.valid_2tuples.append(i)
  
  def create_Ntuples(self):
    # Make N-Tuple or (N+1)-Tuple with valid 2-Tuple
    self.Ntuples = []
    for prod_tuples in product(self.valid_2tuples,repeat=(self.m+1)//2):
      flat_tuple = tuple(chain.from_iterable(prod_tuples))
      if len(flat_tuple) > self.m :
        self.Ntuples.append(flat_tuple[:-1]) # Crop (N+1)-Tuple to append a N-Tuple
      else:
        self.Ntuples.append(flat_tuple)
    # remove duplicates
    self.Ntuples = list(set(self.Ntuples))
  
  def __iter__(self):
    self.create_valid_2tuples()
    self.create_Ntuples()
    return self

  def __next__(self):
    while (self.Ntuples):
      _tuple = self.Ntuples.pop()
      for i in range(self.m-1):
        if (_tuple[i]+_tuple[i+1]) > self.n:
          break
      else:
        return _tuple
    raise StopIteration



# Iterator style
class T_new2:
  def __init__(self, n=1, m=1):
    self.n = n if n>0 else 1
    self.m = m if m>0 else 1
    self.valid_Ntuples = []
  
  def valid_tuple(self, _tuple):
    for i in range(len(_tuple)-1):
      if (_tuple[i]+_tuple[i+1]) > self.n:
        return False
    else:
      return True

  def create_valid_2tuples(self):
    # List all 2-Tuple valid with 'n'
    self.valid_Ntuples = []
    for _tuple in product(range(1,self.n),repeat=2):
      if self.valid_tuple(_tuple) :
        self.valid_Ntuples.append(_tuple)
  
  def create_Ntuples(self):
    # Save higher size N-Tuple to X-Tuple
    croped = False
    if self.valid_Ntuples:
      valid_Xtuples = self.valid_Ntuples
    self.valid_Ntuples = []
    for prod_tuples in product(valid_Xtuples, repeat=2):
      flat_tuple = tuple(chain.from_iterable(prod_tuples))
      # Crop Tuple to append a N-Tuple
      if len(flat_tuple) > self.m :
        flat_tuple = flat_tuple[:-(len(flat_tuple)-self.m)]
        croped = True
      # Valid Tuple
      if self.valid_tuple(flat_tuple):
        self.valid_Ntuples.append(flat_tuple)
    # remove duplicates
    if croped:
      self.valid_Ntuples = list(set(self.valid_Ntuples))
  
  def __iter__(self):
    if self.m >= 2:
      self.create_valid_2tuples()
    while self.m > len(self.valid_Ntuples[0]) :
      self.create_Ntuples()
    return self

  def __next__(self):
    if (self.valid_Ntuples):
      return self.valid_Ntuples.pop()
    raise StopIteration

# Iterator style
class T_roro: # Only for T(4, m)
  def __init__(self, n=1, m=1):
    self.n = n if n>0 else 1
    self.m = m if m>0 else 1
  
  def __iter__(self):
    self.index = 2
    self.Ntuples = [6, 14] # T(4,2), T(4,3)
    return self

  def __next__(self):
    if self.index <= self.m:
      if self.index == 2 :
        self.index = self.index + 1
        return self.Ntuples[0]
      elif self.index == 3 :
        self.index = self.index + 1
        return self.Ntuples[1]
      else:
        self.Ntuples.append(sum(self.Ntuples) + self.Ntuples[-2] + 5)
        self.index = self.index + 1
        return self.Ntuples[-1]
    else:
      raise StopIteration


def main():
    print(40*"=")
    print(Enonce)
    print(40*"-")

    import time
    
    #exercices = [[3,2], [4,2], [5,2], [3,4], [4,4], [5,4], [5, 5], [3, 2], [5, 2], [3, 5], [7, 7], [9, 7], [5, 20]]
    #exercices = [[4, 4]]
    #for n, m in exercices:
    for n, m in [(max , columns) for max in range(3,6) for columns in range(2,11)]:
      start = time.perf_counter()
      Solution = 0
      for i in T(n, m):
        Solution = Solution + 1
      end = time.perf_counter()
      print(f"* T     ({n}, {m})={Solution} en {int(end-start)} secondes")
      
      start = time.perf_counter()
      Solution_new = 0
      for i in T_new(n, m):
        #print(f"Solution {i}")
        Solution_new = Solution_new + 1
      end = time.perf_counter()
      print(f"# T_new ({n}, {m})={Solution_new} en {int(end-start)} secondes")
            
      start = time.perf_counter()
      Solution_new2 = 0
      for i in T_new2(n, m):
        ##print(f"* T_new2({n}, {m})={i}")
        Solution_new2 = Solution_new2 + 1
      end = time.perf_counter()
      print(f"# T_new2({n}, {m})={Solution_new2} en {int(end-start)} secondes")

    #print(40*"*")

##    exercices = [[5, 5]]
##    for n, m in exercices:
##      start = time.perf_counter()
##      Solution = 0
##      for i in T_new(n, m):
##        ##print(i)
##        Solution = Solution + 1
##      end = time.perf_counter()
##      ##print(f"T({n}, {m})={Solution}")
##      print(f"T({n}, {m})={Solution} en {int(end-start)} secondes")

    print(40*"*")

    start = time.perf_counter()
    index = 2
    for i in T_roro(4, 10):
      print(f"# T_roro(4, {index})={i} solutions")
      index = index + 1
    end = time.perf_counter()
    print(f"# T_roro en {int(end-start)} secondes")


    print(40*"-")
    print("Solution = {}".format(Solution_new))
    print(40*"=")

if __name__ == "__main__":
    # execute only if run as a script
    main()
