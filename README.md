# Python Libs

## General

These are just some of the functions that I wrote myself. I didn't write them for external use. I know that there are precompiled binary subroutines in Python that work thousands times faster. I wanted to write these basic functions myself just to prove that I can. That's all.

There's one thing however, that I like about these functions -- since they are open source, you can easily see how they work and **customize them** for your own puroses.

## Python Modules Applied

To use any of these _.py_ files as a functions' library:

1. Fork this repo or Download it as a ZIP file;
2. Put necessary file into your working directory;
3. In your project's _.py_ file use `import filename` to import all functions from the file or `from filename import functionname` to only import a specific function;
4. If you've imported the **whole file** you will have to use dot notation to call functions that it contains;
5. If you've used the second notation to only import **one function**, you can call it buy its name like you would do to a normal function from your file;

```python
# First method -- importing the whole file
import primes
primes.check(13)
```

```python
# Second method -- importing a specific function from the file
from string import reverse
reverse("Hello, world!")
```

## Dictionary

Here I will list all the files, functions inside them and their purposes so that you can know what they contain without having to actually look through each and every file. Filenames I will put in **bold**, functions and classes will be *cursive*.

### combinatorics.py

+ *factorial* --> returns factorial (n!) of given number;
+ *nPr* --> returns number of permutations of n elements for r positions;
+ *nCr* --> returns number of combinations of n elements for r positions;
+ *anagram* --> returns list of every possible arrangement of a given string;

### divisors.py

+ *find* --> returns (a) list of divisors; (b) number of divisors; (c) sum of divisors of a given number;

### fistD.py

+ *class Fist* --> class that may be used to create and interract with final state machines that use binary-based input (string consisting of 0s and 1s);

### graphD.py

+ *class Graph* --> class that may be used to create and interract with undirected graphs where edges don't have values (every edge is as good a path as any other edge);

### listD.py

+ *unsorted* --> returns unsorted array of numbers of given size and given range for numbers' generation;
+ *present_in* --> returns True if element is present in the list given, otherwise returns False;

### logates.py

+ *_not* --> returns the reverse of biary input;
+ *_and* --> returns 1 if both inputs were 1, otherwise returns 0;
+ *_or* --> returns 1 if either of two inputs were 1, otherwise returns 0;
+ *_xor* --> returns 1 if two inputs were different, otherwise returns 0;

(Each of these methods work with inputs longer than one character, for example you can input 10010)

### mathL.py

+ *power* --> returns given number to the given positive power > 1;
+ *fibonacci* --> returns i-th number from fibonacci sequence if i is positive, otherwise returns -1;
+ *mod* --> returns the remainder of division of two given numbers (x % y);
+ *intersect* --> returns the intersection of two given lists or sets;
+ *coprimes* --> returns list of coprimes of a given number;
+ *gcd* --> returns greatest common divisor of two given numbers;
+ *floor* --> returns rounded version of a given number (0.5 --> 1; 0.4 --> 0);

### primes.py

+ *check* --> returns True if number is prime, otherwise returns False;
+ *find* --> returns list of prime numbers less than given limit;
+ *find_distincts* --> returns (a) list of distinct prime divisors; (b) sum of distinct prime divisors of a given number;
+ *find_prime_factors* --> returns list of prime factors of n;

### queueD.py

+ *class Queue* --> implementation of Queue datatype;

### search.py

+ *binary* --> returns index of the element in a given list if found, otherwise returns -1;
+ *linear* --> returns index(s) of the element in a given list if found, otherwise returns -1;

### sort.py

+ *insertion* --> returns sorted list of numbers;
+ *merge* --> returns sorted list of numbers;
+ *bubble* --> returns sorted list of numbers;

### stackD.py

+ *class Stack* --> implementation of Stack datatype;

### stringD.py

+ *reverse* --> returns reversed string;

## Contact

For any personal or business enquiries:

+ Email: *sharp.vik@gmail.com*
+ [Twitter](https://twitter.com/sharp_vik)
+ [VK](https://vk.com/perigrinus)
+ [Instagram](https://www.instagram.com/viktooooor)