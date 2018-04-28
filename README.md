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

Here I will list all the files, functions inside them and their purposes so that you can know what they contain without having to actually look through each and every file. Filenames I will put in **bold**, functions will be *cursive*.

### arrayX.py

+ *unsorted* --> returns unsorted array of numbers of given size and given range for numbers' generation;

### combinatorics.py

+ *factorial* --> returns factorial (n!) of given number;
+ *nPr* --> returns number of permutations of n elements for r positions;
+ *nCr* --> returns number of combinations of n elements for r positions;

### divisors.py

+ *find* --> returns (a) list of divisors; (b) number of divisors; (c) sum of divisors of a given number;

### primes.py

+ *check* --> returns True if number is prime, otherwise returns False;
+ *find* --> returns list of prime numbers less than given limit;
+ *find_distincts* --> returns (a) list of distinct prime divisors; (b) sum of distinct prime divisors of a given number;
+ *find_prime_factors* --> returns list of prime factors of n;

### search.py

+ *binary* --> returns index of the element in a given list if found, otherwise returns -1;
+ *linear* --> returns index(s) of the element in a given list if found, otherwise returns -1;

### sort.py

+ *insertion* --> returns sorted list of numbers;
+ *merge* --> returns sorted list of numbers;
+ *bubble* --> returns sorted list of numbers;

### stringX.py

+ *reverse* --> returns reversed string;

## Contact

For any personal or business enquiries:

+ Email: *sharp.vik@gmail.com*
+ [Twitter](https://twitter.com/sharp_vik)
+ [VK](https://vk.com/perigrinus)
+ [Instagram](https://www.instagram.com/viktooooor)