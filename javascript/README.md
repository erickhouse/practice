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

#### List (Stack and Queue)

```javascript 
list = ['a','b','c','d'] OR list = Array.from("abcd") OR Array(7) 'an array of len 7 with no elements'
```

| Function       | Result | Notes|
| ------------- |-------------|-------------| 
| `[1].concat([2])` | `[1, 2]` | 
| `list.includes('a')` | `true` | 
| `list.length` | `4` | 
| `list.some(elem => elem === 'a')` | `true` | the same thing as any or at least one
| `list.every(elem => elem === 'a')` | `false` | the same thing as all
| `list.push('e')` | `['a','b','c','d','e']` | pushes to the back (stack, queue)
| `list.pop()` | `['a','b','c']` | removes the last element and returns it (stack), undefined if empty
| `list.shift()` | `['b','c','d']` | removes the first element and returns it (queue)

