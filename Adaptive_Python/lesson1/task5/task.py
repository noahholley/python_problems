"""Transform the symbol into uppercase.

Input data

A single symbol.

Output data

If the entered symbol is a lowercase letter of the Latin alphabet, output the same uppercase letter. Otherwise, output the symbol that was entered.


Sample Input:
b
Sample Output:
B


Memory limit: 256 Mb
Time limit: 1s"""

data = input()
if data.isupper():
    print(data)
else:
    print(data.upper())
