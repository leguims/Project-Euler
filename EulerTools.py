"""Function to resolve Euler problems : 
   - Fibonacci (class iterator)
   - PrimeNumber (class iterator)
   - Palindrome (class iterator)
   - Base10Base2Palindrome (class iterator)
   - isPalindrome (function)
"""

import math

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
            for multiple in range(2, math.ceil(math.sqrt(self.current)) + 1):
                if (self.current % multiple == 0) and (self.current != multiple):
                    break
            else:
                return self.nextNumber()
            self.nextNumber()

    def nextNumber(self):
        save = self.current
        self.current = self.current + 2 if self.current != 2 else self.current + 1
        return save


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


# Functions
def isPalindrome(number):
    number_str = str(number)
    #print(f"len(number_str)={len(number_str)} ; number_str={number_str} ; number_str[-1::-1]={number_str[-1::-1]}")
    return (len(number_str) >= 1) and (number_str == number_str[-1::-1])
