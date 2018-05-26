### Big O

http://bigocheatsheet.com/

#### Main ideas

- How does the output behave relative to its input
- Constants don't matter
- Only take the largest factor, the rest become inconsequential as the input becomes very large


```
O(1)

- computation is constant relative to the size of n

```

```
O(n)

 x = n
 while ( x > 0 ) {
     x = x - 1
 }
```

```
O(logn)

 x = n
 while ( x > 0 ) {
     x = x / 2
 }
 
```

```
O(nlogn)

 x = n
 while ( x > 0 ) {
    y = n
    while ( y > 0 ) {
        y = y / 2
    }
    x = x - 1
 }
 
 OR
 
for (i = 1 to N) {
  doSomething(); // takes O(logN)
}

```

```
O(n^2)

 x = n
 while ( x > 0 ) {
    y = n
    while ( y > 0 ) {
        y = y - 1
    }
    x = x - 1
 }
```

```
O(n^2)

 x = n
 while ( x > 0 ) {
    y = n
    while ( y > 0 ) {
        y = y - 1
    }
    x = x - 1
 }
```

```
O(2^n)

- computations double on each step of n
- combinations of all values of n

```

```
O(n!)

- permutations (ordering matters)

```

