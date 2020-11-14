import time
import random
import string
from word_search import WordSearch
#from word_search_2 import WordSearch

# IMPORTANT:
# To run word_search_2, uncomment its import and comment word_search.

# Setting the seed:
random.seed(0)

# Generates a grid of random lowercase characters.
def get_random_grid(length):
    letters = string.ascii_lowercase
    grid = "".join(random.choice(letters) for i in range(length))
    return grid

print("Generating random grid of 10000 by 10000:")

grid = get_random_grid(100000000)

print("Grid generated! Instantiating WordSearch.")

ws = WordSearch(grid)
words_to_find = ["pexip", "random", "odysseas"]

print("words_to_find = ", words_to_find)
print("Starting timing:")

start = time.time()

for word in words_to_find:
    if ws.is_present(word):
        print("found {}".format(word))
    else:
        print("not found {}".format(word))

end = time.time()
print("Time taken = ", end - start)