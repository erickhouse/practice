

## Resources
https://medium.com/@kingrayhan/500-data-structures-and-algorithms-practice-problems-and-their-solutions-b45a83d803f0

https://app.codility.com/programmers/lessons/1-iterations/

### Tools 

- CV compiler that used ML to create the best resume
https://cvcompiler.com/

### Practice
- Hacker Rank
- Leet Code
- Interview Bit
- Byte by Byte
- Interview Cake
- Pramp
- Interviewing.io
- Top Coder
- Coding Dojo
- Cracking the code interview
- Triple Byte
- CodeFights
- RefDash
- Vettery

### Offers
- Hired
- Indeed
- Interview Bit
- LinkedIn
- Triple Byte

### Books
- The Algorithm Design Manual

## The Process

### Algorithms

Both insertion sort and selection sort have an outer loop (over every index), and an inner loop (over a subset of indices). Each pass of the inner loop expands the sorted region by one element, at the expense of the unsorted region, until it runs out of unsorted elements.

The difference is in what the inner loop does:

In selection sort, the inner loop is over the unsorted elements. Each pass selects one element, and moves it to its final location (at the current end of the sorted region).

In insertion sort, each pass of the inner loop iterates over the sorted elements. Sorted elements are displaced until the loop finds the correct place to insert the next unsorted element.

So, in a selection sort, sorted elements are found in output order, and stay put once they are found. Conversely, in an insertion sort, the unsorted elements stay put until consumed in input order, while elements of the sorted region keep getting moved around.

- Bubble Sort
- Merge Sort
- Selection Sort
- Insertion Sort
- Quick Sort
- BFS 
- DFS
- Binary search

### Data Structure
- Tree
  - Binary Tree
  - Binary Search Tree 
  - Red Black Tree
    - Self Balancing 
  - B-Tree
    - A type of binary search tree that can have more than two children 
  - Keywords : Balanced, Levels 
- Graph
  - Directed
  - Weighted
  - Each node may or may not have an edge to another node 
- Queue
- Stack
- Array
- List / Vector
- Linked List
- Matrix
- Heap
- Dict / Map
- Set
- Trie 

### Big O

### Techniques

- Dynamic (Bottom up)
  
- Divide and Conquer (top down)
  - How to solve the sub-instance
  - How to combine the obtained solutions
  - Key words: find, subsets

- Transform and Conquer 
  - Turn the input into something that better fits a solution
  - Compute over multiple passes
  - Key words: pre-sort
  
- Greedy 
  - Take what you can get now. The local optimum 
  - Key words: most, best, optimum, candidates 
  
- Windowed 
  - Move a windowed sub set along the super set, looking for something inside the subset 
  - Keywords: ranges, contains
  
### Problems
 - Determine if two ranges overlap `does [5,10] overlap with [2,3], [6,12]`
 - flatten a dict than contains dicts which may contain sub dicts 

## The Interview

### Helpful hints from the past

- While loops are more flexible, If you aren't sure, default to a while loop. It may save time. Deleting your looping structure after it's been written is quite painful. 

- Focus on solving the problem before writing any code. Run through at least a couple of examples. It is nearly possible to mentally go back to the design phase once you have started coding.

- If the problem requires filtering or a reduction step, don't try and do it in place (return a subset) 

- Telling the interviewer about a problem relating to ambiguity or requirements gathering doesn't seems to matter unless it is very specific to the story. They care about technical implementations, the specific problems faced, and how I overcame then. 
  - Possiblity of using ambiguity if the point is to show abstract problem solving or solving business problems
  
- Make a point to practice optimization (greedy) problems, they come up quite often. 
  - Problems involving local candidates while scanning for the best without being able to know what the remainder of the data set includes
  
- Create a systematic way to break down problem types and their names to quickly reduce the problem space. Read books about algorithms and algorithm types. 


