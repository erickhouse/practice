## JavaScript Cheat Sheet

### General Rules

`let` is block scoped while `var` is function scoped

`for .. in` loops over keys while `for .. of` loops over values

`===` tests for value and type equality while `==` test for equality and will attempt to coerce the types to a common type. 

The 6 types of falsy values

```false — boolean false
0 — number zero
“” — empty string
null
undefined
NaN — Not A Number
```

They have special rules in JS and can have can unexpected results when using loose equality (==)

#### Helpful Functions
```javascript
Math.max(5, 10) // <- 10
Math.max(5, 10) // <- 5

Math.pow(2, 2) <- 4

// spread syntax: spread 'expands' an array into its elements

// can be used to apply an array to a list of arguments
var arr = [1, 2, 3];
Math.max(...arr) // <- 3; ...arr becomes 1, 2, 3

// spread can be used to concat two arrays
var arr1 = [0, 1, 2];
var arr2 = [3, 4, 5];
arr1 = [...arr2, ...arr1]; // <- [3, 4, 5, 0, 1, 2]

// it can be used like a slice
var arr = [1, 2, 3];
var arr2 = [...arr]; // like arr.slice()
arr2.push(4);  // arr uneffected
```

#### List (Stack and Queue)

```javascript 
list = ['a','b','c','d'] OR list = Array.from("abcd") OR Array(7) 'an array of len 7 with no elements'
```

| Function       | Result | Notes|
| ------------- |-------------|-------------| 
| `[1].concat([2])` | `[1, 2]` | This returns a new array. Does not modify the old!
| `list.includes('a')` | `true` | 
| `list.length` | `4` | 
| `list.some(elem => elem === 'a')` | `true` | the same thing as any or at least one
| `list.every(elem => elem === 'a')` | `false` | the same thing as all
| `list.push('e')` | `['a','b','c','d','e']` | pushes to the back (stack, queue)
| `list.pop()` | `['a','b','c']` | removes the last element and returns it (stack), undefined if empty
| `list.shift()` | `['b','c','d']` | removes the first element and returns it (queue)
| `list.splice(0, 1, 'e')` | `['e','b','c','d']` | (startIndex, number of elements to remove, elements to insert)

#### Set

```javascript 
var set = new Set(['a','b','c','d']);
```

| Function       | Result | Notes|
| ------------- |-------------|-------------| 
| `set.add('e')` | `['a','b','c','d','e']` | 
| `set.delete('e')` | `['a','b','c','d']` | 
| `set.has('a')` | `true` | 
| `set.clear()` | `[]` | 
| `set.size` | `4` | 
| `set.values()` | `['a','b','c','d']` | interesting becuase it returns a list of values in insertion order. Might be useful


