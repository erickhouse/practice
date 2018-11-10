

#### Divide and Concur

- Quick Sort & Merge Sort
- Dividing the problem into sub problems and combininig the solutions into a global solution

#### Greedy

Greedy approaches are great because they're fast (usually just one pass through the input). But they don't work for every problem.

How do you know if a problem will lend itself to a greedy approach? Best bet is to try it out and see if it works. Trying out a greedy approach should be one of the first ways you try to break down a new question.

To try it on a new problem, start by asking yourself:

"Suppose we could come up with the answer in one pass through the input, by simply updating the 'best answer so far' as we went. What additional values would we need to keep updated as we looked at each item in our input, in order to be able to update the 'best answer so far' in constant time?"

#### Dynamic

https://medium.com/@codingfreak/top-50-dynamic-programming-practice-problems-4208fed71aa3

*writes down "1+1+1+1+1+1+1+1 =" on a sheet of paper*
"What's that equal to?"
*counting* "Eight!"
*writes down another "1+" on the left*
"What about that?"
*quickly* "Nine!"
"How'd you know it was nine so fast?"
"You just added one more"
"So you didn't need to recount because you remembered there were eight!
Dynamic Programming is just a fancy way to say 'remembering stuff to save time later'"

#### Overlapping subproblems

Given some branching decisions in each state of the loop draw a tree of results. It is possible to see where the inputs from two paths overlap. Useful for recursive or dynamic problems. 

``` python

for state in algorithm:

  if decision 1:
    path1(state)
    
  if decision 2:
    path2(state)

```

In this example it is possible to see where `state` inputs overlap over the algorithm. We can make the decision not to reclaculate a sub state that we have already calculated. 

#### Recursive

#### Branch and Bound

#### Backtracking

Backtracking is a technique used to build up to a solution to a problem incrementally. These "partial solutions" can be phrased in terms of a sequence of decisions. Once it is determined that a "partial solution" is not viable (i.e. no subsequent decision can convert it into a solution) then the backtracking algorithm retraces its step to the last viable "partial solution" and tries again.

Visualizing the decisions as a tree, backtracking has many of the same properties of depth-first search. The difference is that depth-first search will guarantee that it visits every node until it finds a solution, whereas backtracking doesn't visit branches that are not viable.

Because backtracking breaks problems into smaller subproblems, it is often combined with dynamic programming, or a divide-and-conquer approach.

#### Brute Force
  - Look at all possbile combinations

#### Random

#### Top-down vs bottm up

When dealing with a naturally recursive problem we can pick to accumulate results as we go down the stack with a loop or bubble back up with recursion. 

Top-down means to me: go down to the base case from the start of the call stack
Bottom-up means to me: hit the base case and go up the call stack. 

I do not visualize a stack going up when it comes to nested calls. 

an actual stack object makes sense to go "up" and then come back down. Maybe it might be better to reverse my thinking so it is in line with a real stack. 

I should define what unravel means and how to draw it. 

