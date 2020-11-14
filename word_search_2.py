import re
import bisect

# Lenght of rows:
ROW_LENGTH = 10000
# Maximum word size expected to be found:
MAX_WORD_SIZE = 24

class WordSearch(object):

    # Strategy: Split all rows and columns to chunks, mainly of size equal to MAX_WORD_SIZE
    # but also less for substrings near the end of rows or columns of the grid.

    # When dividing the rows and columns into chunks, we use overlapping matches.
    # For example: 

    # let ROW_LENGTH = 5
    # let MAX_WORD_SIZE = 3
    # let grid = "abcdefghij"

    # Then self.grid = ['abc','bcd','cde', 'de', 'e', 'fgh','ghi','hij', 'ij', 'j']

    # We then proceed to sorting self.grid.
    # When is_present(word) is executed, we perform binary search.
    # As a result, run-time complexity is equal to O(log(n))
    

    def __init__(self, grid):
        # Creating a grid array that contains every row and every column as an element.
        # Adding all rows of grid to grid_arr.
        grid_arr = [grid[i:i+ROW_LENGTH] for i in range(0, len(grid), ROW_LENGTH)]
        # Adding all columns of grid to grid_arr.
        grid_arr = grid_arr + [grid[i::ROW_LENGTH] for i in range(0, ROW_LENGTH)]
        
        # List that contains all substrings used by is_present(word)
        self.grid = []

        # Compiling the regex pattern used for splitting string into 
        # overlapping matches of size MAX_WORD_SIZE. 
        regex = re.compile(r"(?=(\w{" + str(MAX_WORD_SIZE) + r"}))")

        # Iterating over every row and column.
        for s in grid_arr:
            # Adding the chunks to self.grid
            self.grid.extend(re.findall(regex, s))

            # Adding chunks of size MAX_WORD_SIZE-1 to 1. 
            # These smaller chunks are from the end of rows and columns.
            for i in range(1, MAX_WORD_SIZE):
                self.grid.append(s[ROW_LENGTH-i:ROW_LENGTH])

        # Sorting self.grid so that we can perform binary search.
        self.grid.sort()


    # If input string word is present in the grid, returns True. Otherwise False.
    def is_present(self, word):

        # Performing binary search on self.grid
        index = bisect.bisect_left(self.grid, word)
        
        # Making sure we are not out of bounds.
        if index < len(self.grid):
            return word in self.grid[index]

        return False

