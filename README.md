# Mathera
Python math module for math-like functions

```python
from mathera import MathFunc as fun

x = fun() # It creates a f(x) = x function
# it means when using this function with operations such as addition and subtraction, it will behave like a variable.

f = x**2 + 4*x + 4
g = x**3

print(f(1), f(2), f(0))
print(g(1), g(2), g(0))
```
[OUT]
```
9 16 4
1 8 0
```


```python
# Mathera also supports function operations
fg = f + g
print( fg(1) ) #>> 10
print( (f+g)(1) ) #>> 10

fog = f(g)
print(fog(2)) #>> 100
print( f(g(2)) ) #>> 100
```
