"""Function to resolve Euler problems : 
   - Fibonacci (class iterator)
   - PrimeNumber (class iterator)
   - Palindrome (class iterator)
   - Base10Base2Palindrome (class iterator)
   - isPalindrome (function)
   - maxGridProduct (function)
"""

import math
from operator import mul
from functools import reduce    

# Iterator style
class Fibonacci:
    """Return Fibonacci number limit by size or highest value"""
    def __init__(self, size=None, highest_value=None):
        self.previous = [0, 1]
        self.index = size
        self.highest_value = highest_value

    def __iter__(self):
        return self

    def __next__(self):
        if self.index is not None:
            if self.index == 0 :
                raise StopIteration
            self.index = self.index - 1
        value = self.previous.pop(0) + self.previous[0]
        self.previous.append(value)
        if self.highest_value is not None:
            if self.highest_value < value :
                raise StopIteration
        return value


class PrimeNumber:
    """Return prime numbers limit by rank or highest value.
    Optimised with 'Problem 7' tips."""
    def __init__(self, rank=None, highest_value=None):
        self.current = 2
        self.index = rank
        self.highest_current = highest_value if highest_value else None

    def __iter__(self):
        return self

    def __next__(self):
        if self.index is not None:
            if self.index == 0 :
                raise StopIteration
            self.index = self.index - 1
        while(True):
            if self.highest_current is not None:
                if (self.highest_current < self.current) :
                    raise StopIteration
            for multiple in range(2, math.ceil(math.sqrt(self.current)) + 1):
                if (self.current % multiple == 0) and (self.current != multiple):
                    break
            else:
                return self.nextNumber()
            self.nextNumber()

    def nextNumber(self):
        save = self.current
        self.current = self.current + 2 if self.current != 2 else 3
        return save

class PrimeFactor:
    """Return prime factors limit by rank or highest value."""
    def __init__(self, highest_value, rank=None):
        self.rest = highest_value
        self.prime_number = PrimeNumber(rank=rank, highest_value=highest_value)

    def __iter__(self):
        self.prime_number.__iter__()
        return self

    def __next__(self):
        while True:
            next_prime_number = self.prime_number.__next__()
            if self.rest%next_prime_number == 0:
                while self.rest%next_prime_number == 0:
                    self.rest = self.rest/next_prime_number
                return next_prime_number
            if self.rest == 1:
                raise StopIteration

class PrimeFactorRepeated:
    """Return all repeated or not prime factors limit by rank or highest value."""
    def __init__(self, rank=None, highest_value=None):
        self.rest = highest_value
        self.prime_number = PrimeNumber(rank=rank, highest_value=highest_value)
        self.current_prime_number = None
        self.current_prime_number_power = None

    def __iter__(self):
        self.prime_number.__iter__()
        return self

    def __next__(self):
        while True:
            if self.current_prime_number :
                if self.rest%self.current_prime_number == 0:
                    self.rest = self.rest/self.current_prime_number
                    self.current_prime_number_power = self.current_prime_number_power + 1
                    return pow(self.current_prime_number, self.current_prime_number_power)
            self.current_prime_number = self.prime_number.__next__()
            self.current_prime_number_power = 0
            if self.rest == 1:
                raise StopIteration


class Palindrome:
    """Construct palindromes (for base 10) between start and end values"""
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


class Base10Base2Palindrome:
    """Construct palindromes for base 10 and 2 between start and end values"""
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


class Pandigital:
    """Construct pandigital between start and end values"""
    def __init__(self, start = 1, end = 9_876_543_210, reverse = False):
        self.start = start
        self.end = end # Max Pandigital number 
        self.reverse = reverse
        self.value = self.start if not self.reverse else self.end

    def __iter__(self):
        return self

    def __next__(self):
        self.value = self.value + 1 if not self.reverse else self.value - 1
        while(True):
            string = str(self.value)
            if (self.value > self.end) or (self.value < self.start):
                raise StopIteration
            for i in string:
                if string.count(i) > 1:
                    self.value = self.value + 1 if not self.reverse else self.value - 1
                    break
            else:
                return self.value


# Functions
def isPrimeNumber(number):
    for multiple in range(2, math.ceil(math.sqrt(number)) + 1):
        if (number % multiple == 0) and (number != multiple):
            return False
    else:
        return True

def isPalindrome(number):
    number_str = str(number)
    #print(f"len(number_str)={len(number_str)} ; number_str={number_str} ; number_str[-1::-1]={number_str[-1::-1]}")
    return (len(number_str) >= 1) and (number_str == number_str[-1::-1])

# Functions
def isCircularPrime(number):
    number_str = str(number)
    circular = [int(number_str[i:]+number_str[0:i]) for i in range(len(number_str))]
    circular_prime = [isPrimeNumber(n) for n in circular]
    #print(f"Circular={circular}")
    #print(f"Circular Prime={circular_prime}")
    return {'isCircularPrime': all(circular_prime), 'CircularPrimeList': circular}

def maxGridProduct(grid, productSize):
    greatest_product = 0
    greatest_factors = []
    for line in grid:
        product, factors = maxLineProduct(line, productSize)
        if product > greatest_product:
            greatest_factors = factors
            greatest_product = product
    return greatest_product, greatest_factors


def maxLineProduct(line, productSize):
    greatest_product = 0
    greatest_factors = []
    index = 0
    max_index = len(line) - productSize
    while index <= max_index:
        factors = line[index : index+productSize]
        #print(f"{index}/{max_index} : {factors}")
        while 0 in factors :
            index = index + 1
            factors = line[index : index+productSize]
        product = reduce(mul, factors, 1)
        if product > greatest_product:
            greatest_factors = factors
            greatest_product = product
        index = index + 1
    return greatest_product, greatest_factors

def transposeGrid(grid):
    return list(zip(*grid)) # transpose grid

def diagonalGrid(grid, topleft_to_bottomright = True):
    """Return Diagonals as a grid from grid"""
    if topleft_to_bottomright:
        gridDiag = [[grid[index][index + offset] for index in range(len(grid) - offset)] for offset in range(len(grid))]
        gridDiag = gridDiag + [[grid[index + offset][index] for index in range(len(grid) - offset)] for offset in range(1, len(grid))]
    else:
        gridDiag = [[grid[index][offset - index] for index in range(offset + 1)] for offset in range(len(grid)-1, -1, -1)]
        gridDiag = gridDiag + [[grid[len(grid)-1 - offset + index][len(grid)-1 - index] for index in range(offset + 1)] for offset in range(len(grid)-2, -1, -1)]
    return gridDiag
