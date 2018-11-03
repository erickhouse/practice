
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
