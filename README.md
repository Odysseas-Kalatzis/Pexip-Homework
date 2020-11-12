# Pexip-Homework
Homework for Pexip. 

Only ```word_search.py``` is required. 

```main.py``` was added to demonstrate how to implement the ```WordSearch``` class. 
Written in Python 3, and the grid size is expected to be **10000 x 10000** characters long as per the instructions.

If a different grid size is used, ```ROW_LENGTH``` from ```word_search.py``` needs to be updated.


## Bonus Question
For this approach, to maximize run time efficiency we rely on the **re** library, written in C and used to pattern match regular expressions. Any other approach relying on scanning the entire string via some loop within Python would yield results several orders slower. This wouldn't be an issue however if we instead used a language designed to have "zero-overhead", such as C++. In such scenario, instead of using a regex library, it may be more efficient to directly implement Knuth–Morris–Pratt algorithm and parallelize it such that different threads pattern match for different rows and columns. This would in theory reduce runtime by a factor of as many threads we're using.
