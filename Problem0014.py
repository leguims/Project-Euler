Enonce = """
Longest Collatz sequence

Problem 14
The following iterative sequence is defined for the set of positive integers:

n -> n/2 (n is even)
n -> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

# Iterator style
class CollatzSequence:
    def __init__(self, start=1):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current == None :
            raise StopIteration
        return self.value()

    def value(self):
        save = self.current
        if self.current == 1 :
            self.current = None
        elif self.current%2 == 0:
            self.current = int(self.current/2)
        else:
            self.current = int(3*self.current+1)
        return save

def main():
    print(40*"=")
    print(Enonce)
    print(40*"-")

    import time

    Solution_Sequence = list([1])
    Solution = 1
    # 1261.26 secondes
    max = 999_999 #100_000 #13
    sequence = list()
    start = time.perf_counter()
    for index in range(max, 0, -1):
        sequence.clear()
        for collatz in CollatzSequence(index):
            sequence.append(collatz)
            if collatz in Solution_Sequence: # End of Collatz sequence already known
                if Solution_Sequence.index(collatz) < sequence.index(collatz):
                    sequence = sequence + Solution_Sequence[Solution_Sequence.index(collatz)+1:]
                    Solution_Sequence = sequence.copy()
                    Solution = index
                    print(f"{round(time.perf_counter()-start,1)}s : New max with {Solution}")
                    print(f"""Length Collatz sequence for {index} = {len(sequence)} :
                    {sequence}""")
                else:
                    sequence.append(f"See Collatz({Solution})")
                break
        #print(f"""Length Collatz sequence for {index} = {len(sequence)} :
        #{sequence}""")
    end = time.perf_counter()
    print(f"{Solution} en {round(end-start,2)} secondes")
    print(f"Length of Collatz sequence with {Solution} = {len(Solution_Sequence)}")
    
    print(40*"-")
    print("Solution = {}".format(Solution))
    print(40*"=")

if __name__ == "__main__":
    # execute only if run as a script
    main()
