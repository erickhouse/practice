
## Arrays and Strings

### Single Riffle Shuffle

I was able to break down the problem and solve the core problem but my original implementation was going to have to keep track of multiple 
indicies. The simple phrase "how does this break down into sub problems" threw me off but made me realize that I could turn this into
recursive problem and keep track of no pointers by popping the front as I went down lists. 

I tried using a flow chart to break down each phrase in the rescursive algorithm. It might be something to consider later. 

```python
def is_single_riffle(half1, half2, shuffled_deck):

    if not half1 and not half2 and not shuffled_deck:
        return True
    
    curr = shuffled_deck.pop(0)
        
    if half1 and half1[0] == curr:
        half1.pop(0)
        return is_single_riffle(half1, half2, shuffled_deck)
        
    if half2 and half2[0] == curr:
        half2.pop(0)
        return is_single_riffle(half1, half2, shuffled_deck)
    
    return False
```

## Dynamic Programming and recursion

### Find 2nd Largest in BST 

I was pretty quickly able to find out the solution but the coding took me longer than it should. It probably took me too long to write the max function. It turns out that I didn't really need to max function. It also doesn't handle the worst case of a descending linked list (all nodes on the lhs). I would end up doing an O(n) operation. 

``` python
def find_second_largest(root_node):

    def getMax(node):
        
        if not node.left and not node.right:
            return node.value
           
        if node.left and not node.right:
            return max(getMax(node.left), node.value)
            
        if node.right and not node.left:
            return max(getMax(node.right), node.value)
            
        return max(getMax(node.left), getMax(node.right), node.value)
            
    def find(node, parent):
        
        if not node.right:
            
            # find max of left
            if node.left and parent:
                return max(getMax(node.left), parent)
            if parent:
                return parent
            if node:
                return node.value
            return None

        return find(node.right, node.value)

    return find(root_node, None)
```
