# LeetCode 36 — Valid Sudoku

## Idea

The board is `9x9`, so I can flatten it into one array of `81` elements.

Mapping:

```python
index = row * 9 + col
row = index // 9
col = index % 9
```

This helped me think of rows, columns, and boxes using indexes.

## What “valid” means

The board does not need to be solved.

We only check:
- no duplicate digits in any row
- no duplicate digits in any column
- no duplicate digits in any `3x3` box
- `"."` is ignored

## Main pattern

For every group:

```python
seen = set()

for value in group:
    if value == ".":
        continue

    if value in seen:
        return False

    seen.add(value)
```

Rows, columns, and boxes are the same idea: check duplicates with a set.

## Rows

Each row is a block of `9` elements:

```text
0..8
9..17
18..26
```

Rows start at:

```python
0, 9, 18, ..., 72
```

## Columns

To move down a column in the flattened array, jump by `9`.

```python
for i in range(col, 81, 9):
```

## 3x3 boxes

Each box starts at:

```python
box_row = 0, 3, 6
box_col = 0, 3, 6
```

Inside a box:

```python
row = box_row + row_shift
col = box_col + col_shift
index = row * 9 + col
```

where:

```python
row_shift = 0, 1, 2
col_shift = 0, 1, 2
```

## Bugs I hit

Do not use `continue` too early if row and column checks are in the same loop, because it can skip column checking.

In a `while` loop, make sure the counter always changes. Otherwise, `"."` + `continue` can cause an infinite loop.

## Clean code lesson

Better:

```python
value = arr[i]

if value != ".":
    if value in seen:
        return False
    seen.add(value)
```

than repeating `arr[i]` many times.

## Keywords

`set`, duplicate check, flattened array, row, column, 3x3 box, index mapping, `row * 9 + col`, ignore dots.
