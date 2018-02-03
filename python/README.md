### Python CheatSheet

#### List (Stack and Queue)

```python 
li = ['a','b','c'], li = list("abc")
```

| Function       | Result | Notes|
| ------------- |-------------|-------------| 
| `enumerate(li)`| `[(1,'a'), (1,'b'), (3,'c')]` | 
| `zip([1,2,3], ['a','b','c'])`| `[(1,'a'), (1,'b'), (3,'c')]` | 
| `[3,1,2].sort()`| `[1,2,3]` | mutates original
| `[1,2] + [3,2]`| `[1,2,3,2]` | 
| `1 in [1,2,3]`| `True` | 
| `[3,1,2].pop()`| `[1,2]` | removes back and returns the value
| `[1,2,3].pop(0)`| `[2,3]` | removes front and returns the value
| `[1,2,3].insert(0,4)`| `[4,1,2,3]` | insert front
| `[1,2,3].append(4)`| `[1,2,3,4]` | push back


#### Dictionary

```python 
d = dict(a=1, b=2, c=3) or d = {'a':1, 'b':2, 'c':3 } or d = dict([(a,1), (b,2), (c,3)])
```

| Function       | Result | Notes|
| ------------- |-------------|-------------| 
| `d.keys()`| `[a,b,c]` | 
| `d.values()`| `[1,2,3]` | 
| `d.items()`| `[(a,1), (b,2), (c,3)]` | 
| `d['a']`| `1` | 
| `d['d'] = 4`| ` {'a':1, 'b':2, 'c':3, 'd:4' }` | 
| `d.pop('c')`| ` {'a':1, 'b':2}` | Throws exception if not found
| `'a' in d`| `True` | 

#### Set

```python 
s = set("abcd"), set = set([1,2,3]), s = {1,2,3}
```

| Function       | Result | Notes|
| ------------- |-------------|-------------| 
| `set([1,2,3]) - set([1,2])`| `{3}` | difference
| `set([1,2,3]) pipe set([1,2,4])`| `{1,2,3,4}` | union
| `set([1,2,3]) & set([1,2,4])`| `{1,2}` | intersection
| `set([1,2,3]).add(4)`| `{1,2,3,4}` | 
| `set([1,2,3]).remove(1)`| `{2,3}` | throw error if not found
| `1 in set([1,2,3])`| `True` | 


#### Matrix

```python
mat = [
     [1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
 ]
```

#### Strings

#### Utils

