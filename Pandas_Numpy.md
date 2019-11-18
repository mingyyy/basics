## Numpy Basics

### Import
`import numpy as np`

The NumPy library takes advantage of a processor feature called **Single Instruction Multiple Data (SIMD)** to process data faster. 
SIMD allows a processor to perform the same operation, on multiple data points, in a single processor cycle.
This concept of replacing for loops with operations applied to multiple data points at once is called **vectorization** and ndarrays make vectorization possible.


### Constructor
- 1-D array
`np.array([1,2,3])`
- 2-D array
`np.array([[1,2],[3,4]])`
- `np.shape(ndarray)` returns a tuple `(number of rows, number of columns)`
- `np[i:j+1]` select every column for row `i` to `j`
- `np[x, y]` select item at row `x` and column `y`

- `np.genfromtxt(filename, delimiter=None)` read file into numpy arrays

### Operators

`vector_a + vector_b`

`vector_a - vector_b`

`vector_a * vector_b`

`vector_a / vector_b`

comparison operators
`<, >, !=, ==`

### Key methods
`vector.min(axia=0)` - calculate the min value of each column

`vector.max(axis=1)` - calculate the max value of each row

`vector.mean()`

`vector.sum()`

`vector.median()`

`vector.dtype()` to see the internal data type

### Boolean Indexing

boolean operation
`np.array([2,4,6,8]) < 5` returns `[True True False False]`
