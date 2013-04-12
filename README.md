# Code-Jam Parser

A quick python module for parsing coding-contest inputs.

Just write a "schema" for the input format and the rest is done for you.
A schema is just a nested structure of functions.

A schema is represented as a list. Within a schema, each element represents a line in the input. Many inputs use a nested structure by first defining the number of test cases, then the format of each test case. `()` represents an `int` that denotes the number of subcases. A subcase is simply represented by a `[]`, which can be thought of as a subschema. See examples for a more detailed explanation.

## Examples
### Simple

Input:

    3
    test string 1
    test string 2
    test string 3

The first line is the number of tests N. N lines follow, each representing test string.

    schema = [(), [str]]

This schema will parse a flat input where the first line denotes the number of testcases and each testcase is a single line in string format. The empty list `[]` defaults to `[str]` so this can be written simply as `schema = [(),[]]`

Result:

    [3, ['test string 1', 'test string 2', 'test string 3']]

### Complex

Input:

    2
    3
    3
    1 2 3
    4 5 6
    7 8 9
    2
    3
    4 3 8
    3 7 1

The first line is the number of test cases.
For each test case, the first line is the number of rows in the matrix and the second line is the number of columns.

    schema = [(), [(), int, [lambda line: map(int, line.split())]]]

The number of columns does not affect the structure of the parse, but is still retained in the structure as an integer. This is an example of how `()` and `int` differ. A subschema must always be accompanied by a `()`. Using this schema, we parse the input as

    [2, [[3, 3, [[1, 2, 3], [4, 5, 6], [7, 8, 9]]], [2, 3, [[4, 3, 8], [3, 7, 1]]]]]
