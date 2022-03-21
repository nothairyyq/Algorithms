# Algorithms
It is very similar to the course of MIT6.046J. The study of algorithms has been applied in a number of different  domains, and to introduce formal concepts of measures of complexity and algorithms analysis.

[Lecture1](https://github.com/nothairyyq/Algorithms/blob/main/6.046J%20%20Lec01.pdf): 

> 1.  Analysis of Algorithms
> 2. Sorting Problem(insertion Sort)
> 3. Running Time Analysis
> 4. Insert Sort & Merge Sort Analysis

[Lecture2](https://github.com/nothairyyq/Algorithms/blob/main/6.046J%20%20Lec02.pdf): 

> 1. Asymptotic Notation:
>    1. Big O
>    2. Big $\Omega $
>    3. Big $\Theta$
> 2. Recurrences
>    1. Substitution-Method
>    2. Recursion-Tree Method
>    3. Master-Method



| Algorithm     |  Time    |Space|  Note    |
| ---- | ---- | ---- |---- |
|  [Insert Sort](Algorithms/Sort/insertionSort.py)    | O(n^2)      |    O(1)  | |
|  [Merge Sort](Algorithms/Sort/mergeSort.py)    | O(n log(n))     |   O(n)  | Divide-Conquer |
| [Selection Sort](Algorithms/Sort/selectionSort.py)      |  O(n^2)   |   O(1)   | |
|[Quick Sort](Algorithms/Sort/quickSort.py)|Best-Case: O(n log(n)) <br> Average-Case O(n log(n)) <br> Worst-Case: O(n^2)| O(log n ) <br> Deepth | Divide and conquer|
|[Randomly Quick Sort](Alogrithms/Sort/random_quickSort.py)|O(n log(n))|Worst: O(n) <br> Best: O(log(n))||
|[Heap Sort]()|O(n logn)|O(1)||
|  [Binary Search](Algorithms/binarySearch)    |  O(log n )    |     | Divide-Conquer |
|  Sequential Search    |      |      | |
|  [power x](Algorithms/power.py)     | O(log n)    |       | Divide-Conquer  |
|Build Heap|O(n)|||
|Heapify|O(log n)|||
|[Activity Selection](https://github.com/nothairyyq/Algorithms/blob/main/Greedy/activitySelection.py)|Sorted: O(n) <br> Not Sorted: O(n logn)||Greedy|
|[Huffman Coding](https://github.com/nothairyyq/Algorithms/blob/main/Greedy/HuffmanCode.py)|Sorted Input: O(n) <br> O(n logn)||Greedy|
|[0-1 Knapsack](https://github.com/nothairyyq/Algorithms/blob/main/Greedy/01Knapsack.py)|O(n logn)|| Greedy <br> Not Found Best|
|[Fibonacci Number](https://github.com/nothairyyq/Algorithms/blob/main/DP/Fibonacci.py)|Recursion: O(2^n) <br> Memory Search: O(n) <br> DP: O(n)||DP|


- [] Activity Selection
- [] Huffman Coding
- [] 0-1 Knapsack Greedy
