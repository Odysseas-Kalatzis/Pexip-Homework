# Pexip-Homework
Homework for Pexip. 

Only ```word_search.py``` and/or ```word_search_2.py``` are required. 

* ```word_search.py``` has an **O(n)** time complexity

* ```word_search_2.py``` has an **O(log(n))** time complexity but requires 24 times more memory than ```word_search.py```.

To run ```word_search_2.py``` on a 10000 by 10000 grid, it requires approximately **15GB** of memory. To avoid using virtual memory, a minimum of 32GB RAM is recommended.

```main.py``` was added to demonstrate how to implement the ```WordSearch``` class.

Written in Python 3, and the grid size is expected to be **10000 x 10000** characters long as per the instructions.

If a different grid size is used, ```ROW_LENGTH``` from ```word_search.py``` and ```word_search_2.py``` needs to be updated.


## Bonus Question
Assuming appropriate hardware, the 2nd solution given with ```word_search_2.py``` should be the one implemented given its logarithmic time complexity. With an implementation written with a systems language that adopts a "zero overhead principle", we can reduce the main bottleneck of this approach, that being memory consumption. By representing characters in ASCII encoding, for a 10000 x 10000 grid ```word_search_2.py``` requires approximately 24 * 2 * 10<sup>8</sup> bytes, which equates to less than 5GB, at least 3 times less than that of Python. Python also suffers from the global interpreter lock which restricts multiple threads from executing Python bytecodes at once. Using a different language that utilizes multi-threaded programming, we can reduce runtime by a factor of as many threads we're using. This is because we can search for different words at different threads.

