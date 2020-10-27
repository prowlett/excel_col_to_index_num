# excel_col_to_index_num

Converts Excel column letter to zero-indexed number

Usage: `excel_col_to_index_num(letter)`

Returns: the number of that column, starting at zero.

Examples:

```
>>> from excel_col_to_index_num import *
>>> excel_col_to_index_num("A")
0
>>> excel_col_to_index_num("Z")
25
>>> excel_col_to_index_num("AA")
26
>>> excel_col_to_index_num("AB")
27
>>> excel_col_to_index_num("ZZ")
701
>>> excel_col_to_index_num("AAA")
702
>>> excel_col_to_index_num("AAB")
703
>>> excel_col_to_index_num("AMJ")
1023
>>> excel_col_to_index_num("ZZZ")
18277
```
