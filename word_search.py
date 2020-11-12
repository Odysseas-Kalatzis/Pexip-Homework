import re

ROW_LENGTH = 10000

class WordSearch(object):
    # Grid is a string of 10**8 characters.
    def __init__(self, grid):
        # The input grid is given in rows being concatenated to each other.
        # We append to the string the same grid but with columns being concatenated.
        # Example: If input grid is abcd, self.grid becomes abcdacbd.

        # This doubles the size in memory, but it pays off in performance since we can 
        # effectively pattern match it using the re library which is implemented in C.  
        self.grid = grid + "".join([grid[i::ROW_LENGTH] for i in range(0, ROW_LENGTH)])

    # If input string word is present in the grid, returns True. Otherwise False.
    def is_present(self, word):
        # Creating a generator that yields the starting and ending index
        # of matching patterns in a tuple.
        gen = ((m.start(), m.end()) for m in re.finditer(word, self.grid))

        # If gen yields no matching pattern, next_gen is assigned to False.
        next_gen = next(gen, False)

        while next_gen:
            # Checking to see if matched pattern lies within different rows or columns.
            if (next_gen[1] - 1 - ((next_gen[1] -1) % ROW_LENGTH)) <= next_gen[0]:
                # A valid pattern of the word is matched to the grid.
                return True
            else:
                # Matched pattern lies within different rows or columns,
                # proceed to next iteration.
                next_gen = next(gen, False)

        # No matched word to self.grid.
        return False
