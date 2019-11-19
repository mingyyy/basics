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
- `np.zeros(number of row, number of col)`

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

boolean operation with other methods
`np.array([2,4,6,8]) < 5` returns `[True True False False]`

- or: `(condition 1) | (condition 2)`
- and: `(condition 1) & (condition 2)`
- not: `~`
- equal `==`
- `any()`
- `all()`

## Pandas

### Construction
`import pandas as pd`

`f500 = pd.read_csv('f500.csv',index_col=0)`

`df.head(n)` and `df.tail(n)`

`df.info()` shows the `dtypes` for each column

`df.loc[row_label, column_label]`

*DataFrames*

| select by label | explicit syntax | shortcut |
| :--------- | ----------- | ----------- |
| single  column | `df.loc[:,"col1"]` | `df["col1"]` |
| list of columns | `df.loc[:, ["col1","col7"]]` | `df["col1","col7"]` |
| slice of columns | `df.loc[:,"col1":"col4"]` | |
| single row | `df.loc["row4"]` | |
| list of rows | `df.loc[["row1", "row8"]]` | |
| slice of rows | `df.loc["row3":"row5"]]` | `df.loc["row3":"row5"]` |

*Series*

| select by label | explicit syntax | shortcut |
| :--------- | ----------- | ----------- |
| single item | `s.loc["item8"]` | `s["item8"]` |
| list of items | `s.loc[["item1","item7"]]` | `s["item1","item7"]` |
| slice of items | `s.loc["item2":"item4"]` | `s["item2": "item4"]` |

### Functions

- `Query` columns (filter rows) of dataframe with boolean expression (Filter based on condition)

`df.query('Age > PassengerId')`: filter all rows which have Age>PassengerId

- `filter`

Filter dataframe on column names or row names (labels) by regrex or just item names

`df.filter(items=['Age', 'Sex'])[:2]`

- `set_index(['col_name1','col_name2'])`

Set any column you want as index of df

- `reset_index()`
Can reset index back to 0....n rows-1

- `rename()`
Renaming column names or row indexes of dataframe. Default is index

`df.rename(columns={'Name': 'Whats_name', 'Fare':'Price'})[:2]`
`df.rename(mapper=str.lower, axis='columns')[:2]`

- `unique()`: Number of unique values in a column of df (Use nunique() for count of unique in each column)
- `duplicated()`: Check duplicated in column. Returns True/False
- `drop_duplicates`: Drop rows which have duplicates
- `groupby`: Group by some column/columns, then we can aggregate to get mean, count, sum or custom function based on the group
`df.groupby(by=[col_name, col_name], level=[0,1].agg({ '': '',
                                                       '': ''}))`
                                                       
- `transform`: Can apply such functions for all columns also using transform which transforms all rows
- `dropna`: Drop rows with na
   `df.dropna(axis=0,  how='any').shape` : row with any column = NA
   `df.dropna(axis=0,  how='all').shape` : row with all columns = NA
   
### Combining data

Inner join 


### Series Vs. DataFrame

Single row and single column are Series; while multi-row and multi-column are data frame.

`series.value_counts()`
`series.max()` - `df.max()`
`series.min()` - `df.min()`
`series.mean()` - `df.mean()`
`series.median()` - `df.median()`
`series.mode()` - `df.mode()`
`series.sum()` - `df.sum()`
`series.describe()` - `df.describe()`


### rename column names - DataFrame
`df.columns=['leader', 'time', 'score']`
 or
`df.rename(columns={'Leader': 'Commander'}, inplace = True)`

### filters
`filter1 = df['date'].between('2019-01-01','2019-06-30')` - date <= '2019-06-30' and >= '2019-01-01'
`filter2 = df['type'].isin(['type1','type2'])` - type is either type1 or type2
`filter3 = df['duration'] == 60` 

`df['new_col'] = df['col'].where(filter1)`
