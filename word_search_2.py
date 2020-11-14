import re
import bisect

ROW_LENGTH = 10000
MAX_WORD_SIZE = 24

class WordSearch(object):

    def __init__(self, grid):
        grid_arr = [grid[i:i+ROW_LENGTH] for i in range(0, len(grid), ROW_LENGTH)]
        grid_arr = grid_arr + [grid[i::ROW_LENGTH] for i in range(0, ROW_LENGTH)]
        
        self.grid = []
        regex = re.compile(r"(?=(\w{" + str(MAX_WORD_SIZE) + r"}))")
        for s in grid_arr:
            self.grid.extend(re.findall(regex, s))
            for i in range(1, MAX_WORD_SIZE):
                self.grid.append(s[ROW_LENGTH-i:ROW_LENGTH])

        self.grid.sort()


    # If input string word is present in the grid, returns True. Otherwise False.
    def is_present(self, word):

        index = bisect.bisect_left(self.grid, word)
        if index < len(self.grid):
            return word in self.grid[index]

        return False

