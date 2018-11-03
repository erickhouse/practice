
Solve the problem simply. Think about how you would solve the problem organically and derive an algorithm from that. 
Don't get too focused on how the algorithm needs to work in code. 

Example (insertion sort)

Think about holding a hand of playing cards. How would you naturally put them in order? Find the lowest playing card and move it to the left.
Then find the next lowest card and place it to the right of the first and so on. Maintaining the swap state in your mind is difficult.

#### Flow chart

- Can the problem be broken down into a flow chart? works well with recursive problems. 

#### BCR

- At the start of a problem think about what the best conceivable runtime is. Generally you can guess off the top of your head. That's what you are optimizing for. 

#### Hueristics

- If you can't find a solution, try assuming that you have a solution and seeing what you can derive from that ("working backward").
  - Sometimes you can build a concrete solution from a simple case but the problem is abstract. Try finding a pattern in the solution. 

#### General tips

- Always start by solving a small instance of the problem by hand. In this problem the recurrence relation and the repetition of function calls become much more obvious when you hand-solve a problem.
- Pay attention to when your solution is computing things you don’t need, like how the naive counting solution generates the sequences but doesn’t actually use them. Reducing unnecessary computation can often provide simpler solutions, if not open the door to more efficient ones.
- Know your recursion. It’s almost useless in most production code because it blasts through the stack, but it’s a very powerful algorithm design tactic. Recursive solutions can often be adapted and improved: the difference between the exponential time naive solution and the linear time nearly-optimal memoization solution is minimal.
- Know your Big-O analysis! You’re practically guaranteed to be asked this at some point during the interview process.
- Always be on the lookout for opportunities to memoize. If your function is deterministic and you’ll be calling it multiple times with the same inputs, your solution may benefit from memoization.
- Find and write out the recurrence relation. In this case writing it out makes it obvious that counts for N hops depend only on counts for N-1 hops.
